# Generated by Django 3.2.6 on 2021-09-11 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Institutes',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=10)),
                ('quota', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Round_2015',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=10)),
                ('opening_rank', models.IntegerField()),
                ('closing_rank', models.IntegerField()),
                ('branch_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.branches')),
                ('institute_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.institutes')),
            ],
        ),
    ]
