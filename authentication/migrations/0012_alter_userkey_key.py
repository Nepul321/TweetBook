# Generated by Django 3.2.9 on 2021-12-18 23:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_alter_userkey_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userkey',
            name='key',
            field=models.CharField(default=uuid.UUID('41386e86-b605-4944-8360-e1986cf6fc43'), max_length=1000),
        ),
    ]
