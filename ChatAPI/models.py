from django.db import models
from django.contrib.auth.models import User


class Pattern(models.Model):
    value = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value

# class CustomResponses(models.Model) :
#     user = models.ForeignKey(User, on_delete=models.CASCADE , default="Guest")
#     tag = models.CharField('title', max_length=1000)
#     responses = models.TextField()
