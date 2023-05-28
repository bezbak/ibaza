# Generated by Django 4.2 on 2023-05-03 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Банк',
                'verbose_name_plural': 'Банк',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('phone', models.CharField(max_length=55)),
                ('instagram', models.URLField()),
                ('address', models.CharField(max_length=255)),
                ('graphic', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=255)),
                ('text', models.TextField(max_length=5555)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Валюта',
                'verbose_name_plural': 'Валюты',
            },
        ),
        migrations.CreateModel(
            name='Exclusives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('litle_text', models.TextField(max_length=255)),
                ('slider', models.FileField(upload_to='slider/')),
                ('number', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Эксклюзив',
                'verbose_name_plural': 'Эксклюзивы',
            },
        ),
        migrations.CreateModel(
            name='Installment_plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('application', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=55)),
                ('last_name', models.CharField(max_length=55)),
                ('number', models.CharField(max_length=55)),
                ('email', models.EmailField(max_length=254)),
                ('passport', models.CharField(max_length=100)),
                ('passport_status', models.CharField(choices=[('ID паспорт', 'ID паспорт'), ('Биометрический паспорт', 'Биометрический паспорт')], default='ID паспорт', max_length=25)),
                ('image', models.FileField(upload_to='passport_img/')),
                ('front_side', models.CharField(max_length=155)),
                ('backside', models.CharField(max_length=100)),
                ('living_place', models.CharField(max_length=100)),
                ('income', models.CharField(max_length=100)),
                ('patent', models.CharField(max_length=255)),
                ('file', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=2000)),
            ],
            options={
                'verbose_name': 'Покупка в рассрочку',
                'verbose_name_plural': 'Покупка в рассрочку',
            },
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Опции',
                'verbose_name_plural': 'Опции',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='product__images/')),
                ('color', models.CharField(max_length=100)),
                ('memory', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=255)),
                ('product_status', models.CharField(choices=[('В наличии', 'В наличии'), ('Нет в наличии', 'Нет в наличии')], default='В наличии', max_length=55)),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_currency', to='products.currency')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='user_images/')),
                ('name', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=550)),
                ('age', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Product_rec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('product_rec', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_rec', to='products.product')),
            ],
            options={
                'verbose_name': 'Рекомендации к товару',
                'verbose_name_plural': 'Рекомендации к товару',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('text', models.CharField(max_length=55)),
                ('order_status', models.CharField(choices=[('Наличными', 'Наличными'), ('Денежный перевод', 'Денежный перевод'), ('Банковский перевод', 'Банковский перевод'), ('Оплата курьеру нв месте', 'Оплата курьеру нв месте'), ('Оплата картой, электронными кошельками на сайте', 'Оплата картой, электронными кошельками на сайте')], default='Наличными', max_length=155)),
                ('contacts', models.CharField(max_length=55)),
                ('name', models.CharField(max_length=55)),
                ('last_name', models.CharField(max_length=55)),
                ('number', models.CharField(max_length=55)),
                ('email', models.EmailField(max_length=254)),
                ('delivery', models.CharField(max_length=55)),
                ('address', models.TextField(max_length=255)),
                ('product_status', models.CharField(choices=[('Самовывоз', 'Самовывоз'), ('Курьер', 'Курьер')], default='Самовывоз', max_length=35)),
                ('comments', models.TextField(max_length=3333)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='country', to='products.country')),
            ],
            options={
                'verbose_name': 'Оформление заказа',
                'verbose_name_plural': 'Оформление заказа',
            },
        ),
        migrations.CreateModel(
            name='Online_calc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('litle_title', models.CharField(max_length=100)),
                ('guarantor', models.BooleanField()),
                ('contribution1', models.CharField(max_length=255)),
                ('loan_terms', models.CharField(max_length=155)),
                ('applications', models.CharField(max_length=155)),
                ('repayment', models.CharField(max_length=100)),
                ('litle_title2', models.CharField(max_length=100)),
                ('term', models.CharField(max_length=255)),
                ('contribution2', models.CharField(max_length=255)),
                ('loan_processing', models.CharField(max_length=155)),
                ('text', models.TextField(max_length=255)),
                ('loan_officer', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=55)),
                ('instagram', models.URLField()),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bank', to='products.bank')),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='online_cur', to='products.currency')),
                ('options', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='options', to='products.options')),
            ],
            options={
                'verbose_name': 'Онлайн калькулятор',
                'verbose_name_plural': 'Онлайн калькулятор',
            },
        ),
    ]