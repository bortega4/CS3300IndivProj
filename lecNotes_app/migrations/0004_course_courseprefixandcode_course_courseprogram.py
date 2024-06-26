# Generated by Django 4.2 on 2024-04-07 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecNotes_app', '0003_alter_course_coursename_lecturer_lecturenotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='coursePrefixAndCode',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='courseProgram',
            field=models.CharField(choices=[('BSNS', 'Business'), ('EAS', 'Engineering and Applied Sciences'), ('LAS', 'Letters, Arts, and Sciences'), ('NHS', 'Nursing and Health Sciences')], default=None, max_length=200),
            preserve_default=False,
        ),
    ]
