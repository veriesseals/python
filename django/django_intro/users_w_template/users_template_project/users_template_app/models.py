from django.db import models

# Create your models here.

# ------------------------------------------------------------------------|
# Create User Model

class User (models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # --------------------------------------------------------------------|
    # property allows the method to be called without parens
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

