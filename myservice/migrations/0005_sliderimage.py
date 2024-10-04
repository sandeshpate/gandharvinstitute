# Generated by Django 5.0.7 on 2024-08-10 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myservice', '0004_rename_description_play_descrip_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='course/image')),
                ('alt_text', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
