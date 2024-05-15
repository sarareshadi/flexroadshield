from django.db import models

# Create your models here.
class Contacts(models.Model):
    full_name = models.CharField(max_length=300)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.full_name}"