from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(max_length=255  )
    logo = models.ImageField(upload_to= 'logo/')
    background = models.FileField(upload_to='background/')
    phone = models.CharField(max_length=20)
    instagram = models.URLField()
    facebook = models.URLField() 
    whats_app = models.URLField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"

    