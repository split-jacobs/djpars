# Generated by Django 2.2.1 on 2019-06-30 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='table_employers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('link', models.URLField()),
                ('name', models.CharField(max_length=30)),
                ('number', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=50)),
                ('date_public', models.CharField(max_length=30)),
            ],
        ),
    ]
