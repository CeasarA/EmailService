from django.db import models

# Create your models here.

class EmailModel(models.Model):
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

class PhoneModel(models.Model):
    phone = models.CharField(max_length=50, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)