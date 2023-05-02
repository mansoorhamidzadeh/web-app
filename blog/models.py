from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone

from account.models import User


class Post(models.Model):
    title=models.CharField(max_length=200)
    file=models.FileField(null=True,blank=True,upload_to='Files')
    content=models.TextField()
    posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bolg:userpost', args=(str(self.author)))