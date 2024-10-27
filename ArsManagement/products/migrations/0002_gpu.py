# Generated by Django 5.1.2 on 2024-10-27 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gpu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_model', models.CharField(max_length=255)),
                ('details', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, default='fallback.png', upload_to='Gpu/')),
            ],
        ),
    ]
