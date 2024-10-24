from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=50, null=False)
    github = models.URLField(max_length=500, null=False)
    linkedin = models.URLField(max_length=500, null=False)
    bio = models.TextField(max_length=500, null=False)

    def __str__(self) -> str:
        return self.name

