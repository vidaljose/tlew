# Generated by Django 3.1.6 on 2021-02-27 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('red', '0002_mensaje_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='url',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]