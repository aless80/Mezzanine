# Generated by Django 2.0.2 on 2018-03-06 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0017_auto_20180305_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
