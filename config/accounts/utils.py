import random
from .models import OTPVerification

# AI prmpts is used by antigravity.(1.6)
def generate_and_save_otp(phone_number):
    otp = str(random.randint(100000, 999999))

    OTPVerification.objects.create(
        phone_number=phone_number,
        otp_code=otp
    )

    return otp