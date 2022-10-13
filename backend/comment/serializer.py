from rest_framework import serializers
from .models import UserComment

class UserCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserComment
        fields = ['user', 'video_id', 'text', 'likes', 'dislikes', 'user_id']
        depth = 1