# Generated by Django 5.0.7 on 2024-08-20 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myservice', '0031_service_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicecard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='posters/img')),
                ('link', models.URLField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]
