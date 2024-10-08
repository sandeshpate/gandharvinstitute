# Generated by Django 5.0.7 on 2024-08-11 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myservice', '0005_sliderimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SlideImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='course/image')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
    ]
