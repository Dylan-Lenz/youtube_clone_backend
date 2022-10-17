from django.urls import path, include
from comments import views

urlpatterns = [
    path('<str:video_id>/', views.get_comments_by_id),
    path('', views.add_comments)
]