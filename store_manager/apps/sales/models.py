from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(db_index=True, unique=True,max_length=200)
    description = models.CharField(blank=True,max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
