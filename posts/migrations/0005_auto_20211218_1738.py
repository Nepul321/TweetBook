# Generated by Django 3.2.9 on 2021-12-18 22:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-datetime']},
        ),
        migrations.RemoveField(
            model_name='post',
            name='time',
        ),
        migrations.AddField(
            model_name='post',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
