# Generated by Django 2.2.2 on 2019-06-26 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20190625_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(default='anonymous', max_length=100),
        ),
    ]
