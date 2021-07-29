from django.db import models

# Create your models here.
class CrudOperation(models.Model):
        name = models.CharField(max_length=40, blank=False, null=False)
        email = models.EmailField(max_length=60, blank=True, null=True)

    
        def __str__(self):
            return self.name