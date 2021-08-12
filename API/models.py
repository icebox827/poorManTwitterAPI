from django.db import models

# Create your models here.
class tweet(models.Model):
    content = models.CharField(max_length=50)
    name = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content