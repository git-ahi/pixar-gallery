# Generated by Django 4.0a1 on 2021-10-12 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_image_post_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-post_time']},
        ),
    ]