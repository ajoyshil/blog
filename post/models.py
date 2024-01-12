from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.name


class Tag(models.Model):
    tag = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.tag


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=80, null=False, blank=False)
    description = models.TextField(blank=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


