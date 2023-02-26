from django.db import models

# Create your models here.
class Note(models.Model):
    """A model representing a typed note"""
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title