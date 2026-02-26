# telegram-otp-login
telegram OTP login using Django

## Project Overview
This project implements an OTP-based authentication system using Django.
Users log in using a One-Time Password (OTP) sent via Telegram instead of passwords.

The project is backend-focused and API-driven.


I am a beginner.
I have created a Django project and an app named "accounts".
Explain in very simple language how OTP-based login works.
Explain OTP generation, expiry time, attempt limit,
and OTP invalidation.
Do not generate full code.

---

## OTP-Based Authentication Concept
OTP (One-Time Password) is a temporary numeric code used for authentication.

In this system:
- User enters a phone number
- Backend generates a 6-digit OTP
- OTP is valid for a limited time
- OTP can be used only once

This improves security and avoids password storage.

---

## OTP Generation, Expiry, and Invalidation
- A secure random 6-digit OTP is generated
- OTP is stored with phone number and timestamp
- OTP expires after 5 minutes
- Each verification attempt increases attempt count
- Once verified, OTP cannot be reused

# A prompt is given using antigravity (1.1)
Adapt the OTP generation and verification logic
to work with an existing Django model named OTPVerification.

Model fields:
- phone_number
- otp_code
- is_verified
- attempts
- created_at

Constraints:
- OTP expires after 5 minutes (use created_at)
- No is_active field exists
- Prevent OTP reuse
- Increment attempts on each verification attempt

Explain what needs to change in the logic.
Do not rewrite the entire code.

---

## Data Model Design
The project uses a single model named OTPVerification.

Stored fields:
- Phone number
- OTP code
- Verification status
- Attempt count
- Creation timestamp

OTP expiry is calculated using the creation time.

# AI promts used by antigravity(1.2)
Generate Django code for an OTP-based login setup using the accounts app.
Requirements:
Create a Django view function named login_page that renders the template accounts/login.html.
Define a Django model named UserOTP.
UserOTP must contain:
phone_number as CharField(max_length=15)
otp as CharField(max_length=6)
created_at as DateTimeField(auto_now_add=True)
Output only valid Django Python code.
Do not include explanations, comments, or extra text.

# AI prompts used by antigravity.(1.3)
I am working on a Django project with an app named "accounts".

Please generate Django model code for a login tracking system.

Requirements:
- A model named LoginHistory
- Fields:
  - phone_number (CharField, max_length=15)
  - status (CharField, max_length=10) to store "success" or "failed"
  - created_at (DateTimeField with auto_now_add=True)
- Implement __str__ method to return:
  "<phone_number> - <status>"
- Follow Django best practices
- Output only the final model code
---

## Backend OTP Logic
### OTP Generation
- Generate random OTP
- Save OTP in database
- Reset verification status and attempts

# A prompt is given using antigravity (1.2)
Create Django logic to generate a 6-digit OTP for phone number login.

Requirements:
- Generate random OTP
- Save OTP in database with expiry time
- Reset previous unused OTPs for same phone number
- Increase attempt count on verification
- Follow Django best practices
Explain the flow clearly.

### OTP Verification
- Check OTP validity
- Verify expiry time
- Increment attempt count
- Mark OTP as verified on success
- Return True or False response

# A prompt is given using antigravity (1.6)
I am building an OTP-based authentication system in Django.

I already have a Django model named `OTPVerification` with the following fields:
- phone_number
- otp_code
- is_verified
- attempts
- created_at

I also have another model named `LoginHistory` with:
- phone_number
- status (success / failed)
- created_at

Please generate a Django helper function named `verify_otp_code(phone_number, input_otp)`.

Requirements:
- Fetch OTP record using phone number
- If OTP record does not exist, mark login as failed and return False
- Check if OTP has expired (5 minutes from created_at)
- If expired, save failed login history and return False
- If OTP matches:
  - Mark OTP as verified
  - Save successful login history
  - Return True
- If OTP does not match:
  - Save failed login history
  - Return False
- Keep logic clean and beginner-friendly
- Do not introduce extra fields or models
- Output only the final function code

---

## API Design
The backend exposes two POST APIs:

- Send OTP  

# AI prompt is used by Antigravity.(1.4)
I am working on a Django project with an app named "accounts".

Please generate a Django view function to send OTP via Telegram.

Context:
- OTP is already generated using a helper function named `generate_and_save_otp(phone_number)`
- Telegram sending is handled by a function `send_otp_via_telegram(chat_id, otp_code)`
- This is a backend-only API (no frontend code)

Requirements:
- Create a view function named `send_otp_view`
- Decorate it with `@csrf_exempt`
- Accept only POST requests
- Read JSON body and extract `phone_number`
- If phone number is missing, return JSON error with HTTP 400
- Generate OTP using `generate_and_save_otp`
- Use a hardcoded Telegram `CHAT_ID` (integer)
- Send OTP via Telegram using `send_otp_via_telegram`
- On success, return JSON: `{ "message": "OTP sent successfully" }`
- If request method is not POST, return HTTP 405
- Use Django best practices
- Output only the final Django view code

- Verify OTP  

# AI prompts is used by antigravity.(1.5)
I am working on a Django project with an app named "accounts".

Please generate a Django view function to verify OTP.

Context:
- OTP verification logic already exists in a helper function named `verify_otp_code(phone_number, otp_code)`
- This is a backend-only API (no frontend code)

Requirements:
- Create a view function named `verify_otp_view`
- Decorate it with `@csrf_exempt`
- Accept only POST requests
- Read JSON body and extract:
  - `phone_number`
  - `otp_code`
- Call `verify_otp_code(phone_number, otp_code)`
- If OTP is valid:
  - Return JSON `{ "status": "success" }`
- If OTP is invalid or expired:
  - Return JSON `{ "status": "error" }` with HTTP 400
- Do not add extra logic
- Use Django best practices
- Output only the final Django view code

All responses are JSON-based.
No frontend code is included.

---

## Telegram Bot Integration
OTP delivery is implemented using Telegram Bot API.

# AI prompts is used by antigravity.(1.6)
I am working on a Django project with an app named "accounts".

Please generate a Django helper function to create and store an OTP.

Context:
- A Django model named `OTPVerification` already exists
- Fields available in the model:
  - phone_number
  - otp_code

Requirements:
- Create a function named `generate_and_save_otp(phone_number)`
- Generate a random 6-digit numeric OTP
- Save the OTP in the `OTPVerification` model with the given phone number
- Return the generated OTP
- Keep the logic simple and clean
- Do not add expiry or verification logic
- Output only the final Python function code

Steps followed:
- Telegram bot created using BotFather
- Bot token obtained securely
- Token stored using environment variables (.env)
- OTP sent using Telegram sendMessage API
- Basic error handling implemented

---

## URL Configuration
- Django admin is enabled
- All API routes are prefixed with `/api/`
- App-level routing is handled inside the accounts app
- Clean separation of project and app URLs

---

## Django Admin Integration
OTPVerification model is registered in Django admin.

Admin panel displays:
- Phone number
- OTP code
- Verification status
- Attempt count
- Creation time

---

## AI Tool Usage (Antigravity)
Antigravity AI was used during development to:
- Understand OTP authentication concepts
- Design OTP expiry and verification logic
- Structure Django APIs
- Document the authentication flow

All AI-generated outputs were reviewed and manually integrated.

---

## Security Considerations
- OTPs are time-limited
- OTPs cannot be reused
- Attempt limits reduce brute-force attacks
- Sensitive credentials are stored securely
- No secrets are committed to GitHub
