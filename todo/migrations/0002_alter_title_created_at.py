# Generated by Django 4.1.3 on 2022-12-02 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2022, 12, 2, 16, 45, 49, 311440, tzinfo=datetime.timezone.utc)),
        ),
    ]