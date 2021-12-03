from django.db import models

# Create your models here.

class ApiData(models.Model):
    text = models.TextField(null=True, blank=True)
    img = models.ImageField(null=True,blank=True,upload_to='media')
    document = models.FileField(null=True,blank=True,upload_to='media')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.text[:10]
    class Meta:
        verbose_name = 'API Data'