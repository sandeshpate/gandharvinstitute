# Generated by Django 5.0.7 on 2024-09-28 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acting', '0003_alter_actingcardslideritem_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actingcardslideritem',
            name='description',
        ),
        migrations.RemoveField(
            model_name='actingcardslideritem',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='actingfee',
            name='text',
            field=models.TextField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='actingfee',
            name='text2',
            field=models.TextField(default=True, null=True),
        ),
    ]
