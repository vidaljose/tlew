# Generated by Django 3.1.6 on 2021-02-27 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('red', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='url',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]