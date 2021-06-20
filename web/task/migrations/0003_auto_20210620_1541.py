# Generated by Django 3.2.4 on 2021-06-20 10:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_template_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='title',
            field=models.CharField(default='Title', max_length=200),
        ),
        migrations.AlterField(
            model_name='template',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 20, 15, 41, 24, 296141), verbose_name='date retrieved'),
        ),
    ]
