# Generated by Django 5.0.1 on 2024-01-18 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotelapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel', models.CharField(max_length=200, unique=True)),
                ('foodname', models.CharField(max_length=200)),
                ('quantity', models.PositiveIntegerField()),
                ('special', models.CharField(max_length=200)),
                ('maxtime', models.PositiveIntegerField()),
                ('delivery', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]