# Generated by Django 3.1.6 on 2021-04-10 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aaltu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='uploads/products/'),
        ),
    ]
