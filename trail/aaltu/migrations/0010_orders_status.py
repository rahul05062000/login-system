# Generated by Django 3.1.6 on 2021-05-20 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aaltu', '0009_auto_20210519_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
