# Generated by Django 3.2.7 on 2021-12-22 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20211221_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uid',
            field=models.IntegerField(default=20),
        ),
    ]
