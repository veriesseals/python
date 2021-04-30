from django.db import models

# Create your models here.
# --------------------------------------------------------------------------------------|
# Create Dojo Model

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # ----------------------------------------------------------------------------------|
    # add discription field
    
    description = models.TextField(default="")
    
    def __str__(self):
        return '{}' .format(self.name)
    
# --------------------------------------------------------------------------------------|
# Create Ninja Model

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo,
                             on_delete=models.CASCADE,
                             related_name='ninjas')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{} {}' .format(self.first_name, self.last_name)