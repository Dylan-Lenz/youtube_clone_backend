from django.db import models
from django.forms import CharField, IntegerField
from authentication.models import User

# Create your models here.
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = CharField(max_length=30)
    text = CharField(max_length=144)