from django.db import models

# Create your models here.
class Currency(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'
        
class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product__images/')
    color = models.CharField(max_length=100)
    memory = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    currency = models.ForeignKey(Currency,related_name='product_currency',on_delete=models.SET_NULL,blank=True,null=True)
    PRODUCT_STATUS = (('В наличии','В наличии'),('Нет в наличии','Нет в наличии'))
    product_status = models.CharField(choices=PRODUCT_STATUS, default='В наличии', max_length=55)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        
class ProductRec(models.Model):
    title = models.CharField(max_length=255)
    product_rec = models.ForeignKey(Product, related_name='product_rec', on_delete=models.SET_NULL,blank=True,null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Рекомендации к товару"
        verbose_name_plural = "Рекомендации к товару"

class Exclusives(models.Model):
    title = models.CharField(max_length=155)
    litle_text = models.TextField(max_length=255)
    slider = models.FileField(upload_to='slider/')
    number = models.IntegerField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Эксклюзив"
        verbose_name_plural = "Эксклюзивы"
        
class Country(models.Model):
    name = models.CharField(max_length=255) 
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
    
        
class Order(models.Model):
    title = models.CharField(max_length=55)
    text = models.CharField(max_length=55)
    ORDER_STATUS = (
        ('Наличными', 'Наличными'),
        ('Денежный перевод', 'Денежный перевод'),
        ('Банковский перевод', 'Банковский перевод'),
        ('Оплата курьеру нв месте', 'Оплата курьеру нв месте'),
        ('Оплата картой, электронными кошельками на сайте', 'Оплата картой, электронными кошельками на сайте'),
    )
    order_status = models.CharField(
        choices=ORDER_STATUS,
        default='Наличными',
        max_length=155
    )
    contacts = models.CharField(max_length=55)
    name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    number = models.CharField(max_length=55)
    email = models.EmailField()
    delivery = models.CharField(max_length=55)
    country = models.ForeignKey(Country, related_name='country', on_delete=models.SET_NULL, blank=True,null=True)
    address = models.TextField(max_length=255)
    PRODUCT_STATUS = (
        ('Самовывоз', 'Самовывоз'),
        ('Курьер', 'Курьер'),
    )
    product_status = models.CharField(
        choices=PRODUCT_STATUS,
        default='Самовывоз',
        max_length=35
    )
    comments = models.TextField(max_length=3333)
    
    def __str__(self):
        return self.contacts
    
    class Meta:
        verbose_name = 'Оформление заказа'
        verbose_name_plural = 'Оформление заказа'
        
class Bank(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Банк'
        verbose_name_plural = 'Банк'
        
class Options(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Опции'
        verbose_name_plural = 'Опции'
    
        
class OnlineCalc(models.Model):
    title = models.CharField(max_length=155)
    litle_title = models.CharField(max_length=100)
    currency = models.ForeignKey(Currency,related_name='online_cur',on_delete=models.SET_NULL, blank=True,null=True)
    guarantor = models.BooleanField(blank=False)  
    contribution1 = models.CharField(max_length=255)
    loan_terms = models.CharField(max_length=155)
    applications = models.CharField(max_length=155)
    repayment = models.CharField(max_length=100)
    litle_title2 = models.CharField(max_length=100)
    bank = models.ForeignKey(Bank, related_name='bank', on_delete=models.SET_NULL,blank=True,null=True)
    options = models.ForeignKey(Options, related_name='options', on_delete=models.SET_NULL,blank=True,null=True)
    term = models.CharField(max_length=255)
    contribution2 = models.CharField(max_length=255)
    loan_processing = models.CharField(max_length=155)
    text = models.TextField(max_length=255)
    loan_officer = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=55)
    instagram = models.URLField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Онлайн калькулятор'
        verbose_name_plural = 'Онлайн калькулятор'
        
class InstallmentPlan(models.Model):
    title = models.CharField(max_length=100)
    application = models.CharField(max_length=100)
    name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    number = models.CharField(max_length=55)
    email = models.EmailField()
    passport = models.CharField(max_length=100)
    PASSPORT_STATUS = (
        ('ID паспорт', 'ID паспорт'),
        ('Биометрический паспорт', 'Биометрический паспорт'),
    )
    passport_status = models.CharField(
        choices=PASSPORT_STATUS,
        default='ID паспорт',
        max_length=25
    )
    image = models.FileField(upload_to='passport_img/')
    front_side = models.CharField(max_length=155)
    backside = models.CharField(max_length=100)
    living_place = models.CharField(max_length=100)
    income = models.CharField(max_length=100)
    patent = models.CharField(max_length=255)
    file = models.CharField(max_length=150)
    description = models.TextField(max_length=2000)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Покупка в рассрочку'
        verbose_name_plural = 'Покупка в рассрочку'
        
class Category(models.Model):
    name = models.CharField(max_length=55)
    currency = models.ForeignKey(Currency,related_name='currency',on_delete=models.SET_NULL,blank=True,null=True)
    product = models.ForeignKey(Product, related_name='product_cat', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    
    
    