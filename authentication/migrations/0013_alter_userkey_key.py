# Generated by Django 3.2.9 on 2021-12-19 00:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_alter_userkey_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userkey',
            name='key',
            field=models.CharField(default=uuid.UUID('35664c4e-b110-4228-89c1-8f181898f19f'), max_length=1000),
        ),
    ]