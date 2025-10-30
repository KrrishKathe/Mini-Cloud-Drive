from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.title
