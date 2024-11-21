from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post(models.Model):
    """
    Defines the schema for the Blog Post table.
    Extends `django.db.models.Model`
    """
    
    class Status(models.TextChoices):
        """
        Defines the status of a post.
        """
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    objects = models.Manager()
    published = PublishedManager()
    
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
    
    def __str__(self):
        """
        Returns the title of the post as a string
        """
        return self.title
