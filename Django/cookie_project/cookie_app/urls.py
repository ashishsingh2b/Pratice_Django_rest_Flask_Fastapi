from django.urls import path
from . import views

urlpatterns = [
    path('set-secure-cookie/', views.set_secure_cookie, name='set_secure_cookie'),
    path('set-signed-cookie/', views.set_signed_cookie, name='set_signed_cookie'),
    path('get-signed-cookie/', views.get_signed_cookie, name='get_signed_cookie'),
    path('set-custom-expiration-cookie/', views.set_custom_expiration_cookie, name='set_custom_expiration_cookie'),
    path('set-session-cookie/', views.set_session_cookie, name='set_session_cookie'),
    path('get-session-cookie/', views.get_session_cookie, name='get_session_cookie'),
    path('delete-session-cookie/', views.delete_session_cookie, name='delete_session_cookie'),
    path('set-json-cookie/', views.set_json_cookie, name='set_json_cookie'),
    path('get-json-cookie/', views.get_json_cookie, name='get_json_cookie'),
]









# from django.urls import path
# from . import views

# urlpatterns = [
#     path("set/", views.set_cookies, name="set_cookie"),
#     path("get/", views.get_cookies, name="get_cookie"),
#     path("del/", views.delete_cookies, name="del_cookie")
# ]
