# Generated by Django 5.0.7 on 2024-08-16 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myservice', '0024_workshop_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workshopnew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=255)),
                ('main_image', models.ImageField(upload_to='workshops/')),
                ('thumbnail1', models.ImageField(upload_to='workshops/')),
                ('thumbnail2', models.ImageField(upload_to='workshops/')),
                ('thumbnail3', models.ImageField(upload_to='workshops/')),
                ('facebook_icon', models.URLField()),
                ('instagram_icon', models.URLField()),
                ('twitter_icon', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='Workshop',
        ),
    ]
