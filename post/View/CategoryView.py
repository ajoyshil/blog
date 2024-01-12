from rest_framework.views import APIView
from rest_framework.response import Response
from post.models import Category
from rest_framework import generics
from post.serializers import CategorySerializer


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []


