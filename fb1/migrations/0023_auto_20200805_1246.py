# Generated by Django 3.0.6 on 2020-08-05 07:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb1', '0022_auto_20200804_0616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagelink', models.CharField(blank=True, max_length=422)),
                ('heading', models.CharField(blank=True, max_length=442)),
                ('body', models.TextField(blank=True)),
                ('date', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='imagepost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 5, 12, 46, 30, 706606)),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 5, 12, 46, 30, 712607)),
        ),
        migrations.AlterField(
            model_name='videopost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 5, 12, 46, 30, 709606)),
        ),
    ]
