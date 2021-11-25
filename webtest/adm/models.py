from django.db import models

# Create your models here.
class article(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    cdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title