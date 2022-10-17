from django.urls import path, include
from comments import views

urlpatterns = [
    path('', views.get_all_comments),
    path('add/', views.user_comments)
]