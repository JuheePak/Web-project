# Generated by Django 3.1 on 2020-09-02 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20200903_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasample',
            name='lat',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='datasample',
            name='lng',
            field=models.FloatField(default=0.0),
        ),
    ]