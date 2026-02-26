from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from datetime import timedelta
import json
import secrets
from .models import OTPVerification, LoginHistory
from .models import LoginHistory
from .telegram_service import send_otp_via_telegram

def login_page(request):
    return render(request, "accounts/login.html")

# AI prompt is used by antigravity.(1.2)
def generate_and_save_otp(phone_number):
    otp_code = f"{secrets.randbelow(1000000):06d}"
    OTPVerification.objects.update_or_create(
        phone_number=phone_number,
        defaults={
            'otp_code': otp_code,
            'is_verified': False,
            'attempts': 0,
            'created_at': timezone.now()
            
        }
    )
    return otp_code
# A prompt is given using antigravity (1.6)

def verify_otp_code(phone_number, input_otp):
    try:
        otp_record = OTPVerification.objects.get(phone_number=phone_number)
    except OTPVerification.DoesNotExist:
        LoginHistory.objects.create(
            phone_number=phone_number,
            status="failed"
        )
        return False

    # expiry check (5 minutes)
    if timezone.now() > otp_record.created_at + timedelta(minutes=5):
        LoginHistory.objects.create(
            phone_number=phone_number,
            status="failed"
        )
        return False

    if otp_record.otp_code == input_otp:
        otp_record.is_verified = True
        otp_record.save()

        LoginHistory.objects.create(
            phone_number=phone_number,
            status="success"
        )
        return True

    # wrong OTP
    LoginHistory.objects.create(
        phone_number=phone_number,
        status="failed"
    )
    return False


  
# AI prompts is used by Antigravity.(1.4)
@csrf_exempt
def send_otp_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        phone = data.get("phone_number")

        if not phone:
            return JsonResponse({"error": "Phone number required"}, status=400)

        otp_code = generate_and_save_otp(phone)

        CHAT_ID = 6006031150  # <-- apna chat id
        send_otp_via_telegram(CHAT_ID, otp_code)

        return JsonResponse({"message": "OTP sent successfully"})

    return JsonResponse({"error": "Invalid request"}, status=405)

# AI prompts is used by Antigravity.(1.5)

@csrf_exempt
def verify_otp_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        phone_number = data.get('phone_number')
        otp_code = data.get('otp_code')

        if verify_otp_code(phone_number, otp_code):
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error'}, status=400)
        


def login_history_view(request, phone_number):
    history = LoginHistory.objects.filter(
        phone_number=phone_number
    ).order_by('-created_at')

    data = []
    for h in history:
        data.append({
            "status": h.status,
            "login_time": h.created_at.strftime("%Y-%m-%d %H:%M:%S")
        })

    return JsonResponse({"history": data})