# Generated by Django 3.2.9 on 2021-12-18 22:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_alter_userkey_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userkey',
            name='key',
            field=models.CharField(default=uuid.UUID('55cb605f-31a3-470f-b472-0f9026d6e733'), max_length=1000),
        ),
    ]
