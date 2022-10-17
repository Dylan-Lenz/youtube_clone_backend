from django.urls import path, include
from backend.comments.views import user_comments
from comments import views

urlpatterns = [
    path('all/', views.get_all_comments),
    path('', views.user_comments)
]