# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.

# def set_cookies(request):
#     response =HttpResponse("Cookies Has been sent")
#     response.set_cookie("user_name","Ashish", max_age=3600)
#     return response

# def get_cookies(request):
#     user_name= request.COOKIES.get("user_name","Guest")
#     return HttpResponse(f"Hello,{user_name}")

# def delete_cookies(request):
#     response=HttpResponse("Cookies Deleted")
#     response.delete_cookie('user_name')
#     return response
# views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.core.signing import Signer
import json
import datetime

# 1. Secure Cookie
def set_secure_cookie(request):
    response = HttpResponse("Secure cookie has been set!")
    response.set_cookie("secure_user", "Ashish", max_age=3600, secure=True, httponly=True)
    return response

# 2. Signed Cookie
signer = Signer()

def set_signed_cookie(request):
    signed_value = signer.sign("Ashish")
    response = HttpResponse("Signed cookie has been set!")
    response.set_cookie("signed_user", signed_value, max_age=3600)
    return response

def get_signed_cookie(request):
    signed_value = request.COOKIES.get("signed_user", None)
    if signed_value:
        try:
            original_value = signer.unsign(signed_value)
            return HttpResponse(f"Hello, {original_value}")
        except Exception:
            return HttpResponse("Invalid cookie value!")
    return HttpResponse("No signed cookie found.")

# 3. Custom Expiration Cookie
def set_custom_expiration_cookie(request):
    expires_at = datetime.datetime.strftime(
        datetime.datetime.utcnow() + datetime.timedelta(days=1), "%a, %d-%b-%Y %H:%M:%S GMT"
    )
    response = HttpResponse("Cookie with custom expiration set!")
    response.set_cookie("custom_expire_user", "Ashish", expires=expires_at)
    return response

# 4. Session Cookie
def set_session_cookie(request):
    request.session['user_name'] = "Ashish"
    return HttpResponse("Session cookie has been set!")

def get_session_cookie(request):
    user_name = request.session.get('user_name', 'Guest')
    return HttpResponse(f"Hello, {user_name}")

def delete_session_cookie(request):
    request.session.flush()
    return HttpResponse("Session cookie deleted!")

# 5. JSON Cookie
def set_json_cookie(request):
    data = {"user_name": "Ashish", "role": "admin"}
    response = HttpResponse("JSON cookie has been set!")
    response.set_cookie("user_data", json.dumps(data), max_age=3600)
    return response

def get_json_cookie(request):
    user_data = request.COOKIES.get("user_data", None)
    if user_data:
        data = json.loads(user_data)
        return HttpResponse(f"Hello, {data['user_name']}, Role: {data['role']}")
    return HttpResponse("No JSON cookie found.")

# 6. Custom Middleware Cookie Example
class CustomCookieMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if "visited" not in request.COOKIES:
            response.set_cookie("visited", "true")
        return response
