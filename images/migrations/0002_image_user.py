# Generated by Django 3.2.4 on 2021-06-25 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='user',
            field=models.CharField(default=' ', max_length=15),
            preserve_default=False,
        ),
    ]
