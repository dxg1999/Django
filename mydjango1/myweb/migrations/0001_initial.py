# Generated by Django 3.1.1 on 2020-09-11 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('selfimg', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('faculty', models.CharField(max_length=100)),
            ],
        ),
    ]