# Generated by Django 3.1.6 on 2021-04-10 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aaltu', '0002_auto_20210410_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=23)),
            ],
        ),
    ]
