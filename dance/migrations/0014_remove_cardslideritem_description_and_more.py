# Generated by Django 5.0.7 on 2024-09-28 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dance', '0013_alter_cardslideritem_subtitle_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardslideritem',
            name='description',
        ),
        migrations.RemoveField(
            model_name='cardslideritem',
            name='subtitle',
        ),
    ]
