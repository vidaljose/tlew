# Generated by Django 3.1.6 on 2021-02-27 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('red', '0004_mensaje_delete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensaje',
            old_name='delete',
            new_name='deleted',
        ),
    ]
