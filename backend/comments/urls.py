from django.urls import path, include
from comments import views

urlpatterns = [
    path('<str:>/', views.get_comments_by_id),
    path('', views.user_comments)
]