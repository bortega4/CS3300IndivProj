# Generated by Django 4.2 on 2024-04-07 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursePrefix', models.CharField(max_length=200)),
                ('courseCode', models.IntegerField(max_length=4)),
                ('courseName', models.CharField(max_length=200)),
                ('courseLecturer', models.CharField(max_length=200)),
            ],
        ),
    ]
