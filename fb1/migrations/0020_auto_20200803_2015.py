# Generated by Django 3.0.6 on 2020-08-03 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb1', '0019_auto_20200803_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcomment',
            name='name',
        ),
        migrations.AlterField(
            model_name='imagepost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 3, 20, 15, 15, 317618)),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 3, 20, 15, 15, 322618)),
        ),
        migrations.AlterField(
            model_name='videopost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 3, 20, 15, 15, 320618)),
        ),
    ]