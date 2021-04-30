from django.db import models

# Create your models here.
# --------------------------------------------------------------|
# book model

class Book(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
# --------------------------------------------------------------|
# author model

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name= models.CharField(max_length=45)
    notes = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    books = models.ManyToManyField('Book', related_name='authors')
    
    @property
    def full_name(self):
        return f"{self.first_name}{self.last_name}"


