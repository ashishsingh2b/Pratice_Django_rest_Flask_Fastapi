#################file based session #########################

from django.shortcuts import render
from django.http import HttpResponse

# Set session data with expiry time of 20 seconds
def set_session(request):
    request.session['username'] = 'John'
    request.session.set_expiry(300)  # Set expiry time to 20 seconds
    return HttpResponse("File-based session data set with 5 minutes seconds expiry.")

# Get session data and extend expiry time if session exists
def get_session(request):
    if 'username' in request.session:
        username = request.session['username']
        # Extend expiry time by 20 seconds on each request
        request.session.set_expiry(300)
        return HttpResponse(f"Hello, {username}! Session expiry extended.")
    else:
        return HttpResponse("No session data found.")

# Delete session data
def delete_session(request):
    try:
        del request.session['username']
        return HttpResponse("Session data deleted.")
    except KeyError:
        return HttpResponse("No session data to delete.")



#####################Sessin extending#############################

# from django.shortcuts import render
# from django.http import HttpResponse
# from datetime import datetime

# # Set session data with expiry time of 20 seconds
# def set_session(request):
#     request.session['username'] = 'John'
#     request.session.set_expiry(20)  # Set expiry time to 20 seconds
#     return HttpResponse("Session data set with 20 seconds expiry.")

# # Get session data and extend expiry time if session exists
# def get_session(request):
#     if 'username' in request.session:
#         username = request.session['username']
#         # Extend expiry time by 20 seconds on each request
#         request.session.set_expiry(20)
#         return HttpResponse(f"Hello, {username}! Session expiry extended.")
#     else:
#         return HttpResponse("No session data found.")

# # Delete session data
# def delete_session(request):
#     try:
#         del request.session['username']
#         return HttpResponse("Session data deleted.")
#     except KeyError:
#         return HttpResponse("No session data to delete.")





###################### session #################


# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.

# # ✅ Set Session Data with Expiry
# def set_session(request):
#     request.session['username'] = 'John'
#     request.session.set_expiry(50)  # Expires after 20 seconds
#     return HttpResponse('Session Data Set')

# # ✅ Get Session Data
# def get_session(request):
#     username = request.session.get('username', 'guest')
#     return HttpResponse(f"Hello, {username}")

# # ✅ Delete Session Data
# def delete_session(request):
#     try:
#         del request.session['username']
#     except KeyError:
#         pass
#     return HttpResponse('Session Data Deleted')

# ✅ Get Session Keys
def session_keys(request):
    keys = request.session.keys()
    return HttpResponse(f"Session Keys: {list(keys)}")

# ✅ Get Session Items
def session_items(request):
    items = request.session.items()
    return HttpResponse(f"Session Items: {dict(items)}")

# ✅ Set Default Session Data
def session_setdefault(request):
    username = request.session.setdefault('username', 'guest')
    return HttpResponse(f"Default Username: {username}")

# ✅ Clear All Session Data
def session_clear(request):
    request.session.clear()
    return HttpResponse('All Session Data Cleared')

# ✅ Flush Session Data (Deletes session completely)
def session_flush(request):
    request.session.flush()
    return HttpResponse('Session Data Flushed')

# Set a test cookie
def set_test_cookie(request):
    request.session.set_test_cookie()
    return HttpResponse("Test cookie set.")

# Check if the test cookie worked
def test_cookie_worked(request):
    if request.session.test_cookie_worked():
        return HttpResponse("Test cookie is working!")
    else:
        return HttpResponse("Test cookie is not working.")

# Delete the test cookie
def delete_test_cookie(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        return HttpResponse("Test cookie deleted successfully.")
    else:
        return HttpResponse("No test cookie was set.")
