from django.db import models

# Create your models here.
class utilisateur(models.Model):
    """Model definition for utilisateur."""

    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=255)
    images = models.ImageField(upload_to='image_user',default='default.jpg')
    password = models.CharField(max_length=255)
    password1 = models.CharField(max_length=255)
    date_add = models.DateField(auto_now=False, auto_now_add=False, null=True)
    date_update = models.DateField(auto_now=False, null=True)
    staut = models.BooleanField(default=True)

    class Meta:
        """Meta definition for utilisateur."""

        verbose_name = 'utilisateur'
        verbose_name_plural = 'utilisateurs'

    def __str__(self):
        """Unicode representation of utilisateur."""
        return self.name
