# Generated by Django 3.2.9 on 2021-12-18 22:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_userkey_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userkey',
            name='key',
            field=models.CharField(default=uuid.UUID('7cf9efdc-9ab8-4cdb-94f5-261689906da6'), max_length=1000),
        ),
    ]
