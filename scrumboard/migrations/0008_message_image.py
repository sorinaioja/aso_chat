# Generated by Django 3.2.8 on 2021-11-28 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0007_message_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
