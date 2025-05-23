# Generated by Django 5.2.1 on 2025-05-17 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, upload_to='menu_images/')),
                ('stripe_product_id', models.CharField(blank=True, max_length=255, null=True)),
                ('stripe_price_id', models.CharField(blank=True, max_length=255, null=True)),
                ('preparation_process', models.TextField(blank=True, max_length=1000)),
                ('farm_name', models.CharField(blank=True, max_length=255)),
                ('farm_address', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
