from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

# Dieses Projekt ist mit https://tutorial-extensions.djangogirls.org/en/homework_create_more_models/ Django-Girls Tutorial
# Schritt - für - Schritt geschrieben


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    #The related_name option in models.ForeignKey allows us to have access to comments from within the Post model.
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField(max_length=1000, blank=False, editable=True)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False) #im Admin-Panel ist das eine leere (False) Checkbox

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

