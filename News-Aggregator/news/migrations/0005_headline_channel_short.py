# Generated by Django 3.2.9 on 2021-12-03 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20211203_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='headline',
            name='channel_short',
            field=models.CharField(default='default', max_length=30),
            preserve_default=False,
        ),
    ]