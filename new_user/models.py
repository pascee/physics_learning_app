from django.db import models

class User(models.Model):
    teacher_yn = models.BooleanField()
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    
