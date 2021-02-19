from django.urls import path
from . import views

app_name = 'group'

urlpatterns = [
    path('group_main/', views.group_main, name="group_main"),
    path('modify/', views.group_modify, name="group_modify"),
    path('group_signin/', views.group_signin, name="group_signin"),
    path('group_login/', views.group_login, name="group_login"),
    path('group_del_member/<int:user_id>/', views.group_del_member, name="group_del_member")
]
