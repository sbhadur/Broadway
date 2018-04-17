# Generated by Django 2.0.4 on 2018-04-17 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_auto_20180417_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adduseractivity',
            name='user',
        ),
        migrations.AddField(
            model_name='adduseractivity',
            name='activity_user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity_user', to='user.Profile'),
        ),
        migrations.AlterField(
            model_name='addmovieactivity',
            name='movie',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie', to='main.Movie'),
        ),
    ]