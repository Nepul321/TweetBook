# Generated by Django 3.2.9 on 2021-12-18 22:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_userkey_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userkey',
            name='key',
            field=models.CharField(default=uuid.UUID('51720bb3-8d92-497b-999c-47b5734e5bc1'), max_length=1000),
        ),
    ]
