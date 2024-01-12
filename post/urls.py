from django.urls import path
from .View import PostView, CategoryView, TagView

urlpatterns = [

    path('posts/', PostView.PostView.as_view()),
    path('categories/', CategoryView.CategoryView.as_view()),
    path('tags/', TagView.TagView.as_view()),

]
