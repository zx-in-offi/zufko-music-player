# Generated by Django 2.2.4 on 2021-01-13 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='duration',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
    ]