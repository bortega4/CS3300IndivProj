# Generated by Django 4.2 on 2024-04-27 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lecNotes_app', '0012_alter_lecturenotes_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturenotes',
            name='user',
        ),
    ]
