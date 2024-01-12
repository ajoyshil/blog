from rest_framework.views import APIView
from rest_framework.response import Response
from post.models import Tag
from rest_framework import generics
from post.serializers import TagSerializer


class TagView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = []

