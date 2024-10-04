# Generated by Django 5.0.7 on 2024-08-12 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myservice', '0017_coursecontent_alter_feature_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecontent',
            name='image_url',
            field=models.ImageField(upload_to='course/image'),
        ),
        migrations.AlterField(
            model_name='coursecontent',
            name='paragraph',
            field=models.TextField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='coursecontent',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='coursecontent',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
