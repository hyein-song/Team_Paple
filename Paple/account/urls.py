from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('signup_done/', views.signupdone, name="signup_done"),
    path('login/', views.login, name='login'),
    path('modify/', views.modify, name='modify'),
]
