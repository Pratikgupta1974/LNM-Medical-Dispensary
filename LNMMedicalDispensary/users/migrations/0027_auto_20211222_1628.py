# Generated by Django 3.2.8 on 2021-12-22 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chemist',
            name='phonenumber',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phonenumber',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phonenumber',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]