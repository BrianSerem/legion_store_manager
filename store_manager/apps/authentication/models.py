from datetime import datetime, timedelta
from django.conf import settings

from django.db import models


class User:
  
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    role = models.EmailField(db_index=True, unique=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    

    def __str__(self):
       
        return self.email

    @property
    def get_full_name(self):
       
        return self.username

    def get_short_name(self):
       
        return self.username