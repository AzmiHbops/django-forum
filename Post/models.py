from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date='published', blank=True)
    detail = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='posts')
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default='draft')
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    class Meta:
        ordering = ('-published',)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post:detail", kwargs={"pk": self.pk, "slug":self.slug})
    
    def __str__(self):
        return self.title
    
