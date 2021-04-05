from django.db import models

# Create your models here.

# -------------------------------------------------------------------------|
# Create User Class

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField(unique = True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # ---------------------------------------------------------------------|
    # Create method to return data in readable format
    def __str__(self):
        return '{} {}' .format(self.first_name, self.last_name)

