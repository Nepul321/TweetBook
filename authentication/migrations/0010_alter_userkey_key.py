# Generated by Django 3.2.9 on 2021-12-18 22:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_alter_userkey_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userkey',
            name='key',
            field=models.CharField(default=uuid.UUID('1a747fcd-ed63-4963-8d1b-eea9e440810b'), max_length=1000),
        ),
    ]
