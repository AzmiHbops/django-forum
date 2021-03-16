from django.db import models
from Post.models import Post

# Create your models here.

class Comment(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive')
    )
    name = models.CharField(max_length=55)
    email = models.EmailField(max_length=75)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="inactive")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.TextField()

    def __str__(self):
        return f"{self.name} {self.body[:25]}"
        
        


