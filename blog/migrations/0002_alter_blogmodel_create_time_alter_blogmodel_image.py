# Generated by Django 4.2.1 on 2023-05-05 10:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 5, 10, 47, 1, 906002, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='image',
            field=models.ImageField(upload_to='cover_blog/'),
        ),
    ]