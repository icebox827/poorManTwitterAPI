from django.db import models

# Create your models here.
class tweet(models.Model):
    content = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=15)