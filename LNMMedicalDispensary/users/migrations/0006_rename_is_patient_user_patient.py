# Generated by Django 3.2.7 on 2021-11-15 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_is_patient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_patient',
            new_name='patient',
        ),
    ]