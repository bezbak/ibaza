from django.db import models
        
        
class Reviews(models.Model):
    image = models.ImageField(upload_to='user_images/')
    name = models.CharField(max_length=100)
    text = models.CharField( max_length=550)
    age = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        

class Contact(models.Model):
    title = models.CharField(max_length=55)
    phone = models.CharField(max_length=55,)
    instagram = models.URLField()
    address = models.CharField(max_length=255)
    graphic = models.CharField(max_length=50,  null=True)
    name = models.CharField(max_length=255)
    text = models.TextField(max_length=5555)
    email = models.EmailField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
    