# Generated by Django 5.0.7 on 2024-08-09 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myservice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classcard',
            name='image_class',
            field=models.ImageField(max_length=50, upload_to='course/image'),
        ),
        migrations.AlterField(
            model_name='classcard',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
