# Generated by Django 2.0.4 on 2018-04-17 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('user', '0021_auto_20180417_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('activity_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity_user', to='user.Profile')),
                ('main_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_user', to='user.Profile')),
                ('movie', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie', to='main.Movie')),
            ],
        ),
        migrations.RemoveField(
            model_name='abstractactivity',
            name='main_user',
        ),
        migrations.RemoveField(
            model_name='addmovieactivity',
            name='abstractactivity_ptr',
        ),
        migrations.RemoveField(
            model_name='addmovieactivity',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='adduseractivity',
            name='abstractactivity_ptr',
        ),
        migrations.RemoveField(
            model_name='adduseractivity',
            name='activity_user',
        ),
        migrations.DeleteModel(
            name='AbstractActivity',
        ),
        migrations.DeleteModel(
            name='AddMovieActivity',
        ),
        migrations.DeleteModel(
            name='AddUserActivity',
        ),
    ]
