from django.db import models


class Ticket(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    screenshot = models.ImageField(upload_to="screenshots/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
