from django.urls import path
from user_session import views

urlpatterns = [
    path('set-session/', views.set_session, name='set_session'),
    path('get-session/', views.get_session, name='get_session'),
    path('delete-session/', views.delete_session, name='delete_session'),
    path('session-keys/', views.session_keys, name='session_keys'),
    path('session-items/', views.session_items, name='session_items'),
    path('set-default/', views.session_setdefault, name='session_setdefault'),
    path('clear-session/', views.session_clear, name='session_clear'),
    path('flush-session/', views.session_flush, name='session_flush'),
    path('set-test-cookie/', views.set_test_cookie, name='set_test_cookie'),
    path('test-cookie-worked/', views.test_cookie_worked, name='test_cookie_worked'),
    path('delete-test-cookie/', views.delete_test_cookie, name='delete_test_cookie'),
]
