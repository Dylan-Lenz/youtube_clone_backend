from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Comments
from .serializers import CommentSerializer

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_comments(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_comments_by_id(request, video_id):
    video_id = Comments.objects.filter(video_id=request)
    serializer = CommentSerializer(video_id, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)