# Generated by Django 5.0.3 on 2024-05-14 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_delete_populardestinaion'),
    ]

    operations = [
        migrations.CreateModel(
            name='popularDestinaion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='PopularDestination')),
                ('nameOfImage', models.CharField(max_length=100)),
                ('search_name', models.CharField(max_length=100)),
                ('discount', models.IntegerField()),
            ],
        ),
    ]