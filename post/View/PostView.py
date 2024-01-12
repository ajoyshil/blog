from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from post.models import Post
from rest_framework import generics
from post.serializers import PostSerializer


class PostView(generics.ListCreateAPIView):

    serializer_class = PostSerializer


    def get_queryset(self):
        query = self.request.GET.get('query', '')
        print(query)
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(category__name__icontains=query) |
            Q(tags__tag__icontains=query)
        ).distinct()
        return posts
