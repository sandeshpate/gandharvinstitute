# Generated by Django 5.0.7 on 2024-08-11 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myservice', '0006_aboutusinfo_slideimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='course/image')),
                ('alt_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SliderTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='course/image')),
                ('alt_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='AboutUsInfo',
        ),
        migrations.DeleteModel(
            name='SlideImage',
        ),
    ]
