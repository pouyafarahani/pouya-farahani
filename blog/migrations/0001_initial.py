# Generated by Django 4.2.1 on 2023-05-05 07:47

import datetime
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime(2023, 5, 5, 7, 47, 51, 325988, tzinfo=datetime.timezone.utc))),
                ('image', models.ImageField(upload_to='media/')),
                ('title', models.CharField(max_length=500)),
                ('description', tinymce.models.HTMLField()),
                ('short_description', models.CharField(max_length=500)),
            ],
        ),
    ]