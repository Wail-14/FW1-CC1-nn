from django.db import models

class Collec(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    date = models.DateField(null=False)

    def __str__(self):
        return self.title
