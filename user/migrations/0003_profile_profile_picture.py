# Generated by Django 2.0.4 on 2018-04-13 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='static/assets/user_images/default.png', upload_to='static/assets/user_images/'),
        ),
    ]
