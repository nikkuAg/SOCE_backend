# Generated by Django 3.2.6 on 2021-10-02 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_auto_20211002_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institutes',
            name='phone',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
