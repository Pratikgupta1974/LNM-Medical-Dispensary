# Generated by Django 3.2.7 on 2021-11-14 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211114_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_chemist',
            field=models.BooleanField(default=False, verbose_name='Is chemist'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_doctor',
            field=models.BooleanField(default=False, verbose_name='Is doctor'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_patient',
            field=models.BooleanField(default=False, verbose_name='Is patient'),
        ),
    ]