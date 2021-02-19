from django.urls import path
from . import views

app_name = 'bbs'

urlpatterns = [
    path('main/', views.main, name='main'),
    path('logout/', views.logout, name='logout'),
    path('board/', views.board, name='board'),
    path('board/<int:post_id>/', views.detail, name='detail'),
    path('board/<int:post_id>/comment/', views.comment_register, name='comment_register'),
    path('board/<int:post_id>/update/', views.post_update, name='post_update'),
    path('board/<int:post_id>/delete/', views.post_delete, name='post_delete'),
    path('board/register/', views.post_register, name='post_register'),
    path('board/register2/<int:q_id>', views.post_register2, name='post_register2'),
    path('board/<int:q_id>/register/', views.question_register, name='question_register'),
    path('board/<str:q_date>/register2/', views.question_register2, name='question_register2')
]
