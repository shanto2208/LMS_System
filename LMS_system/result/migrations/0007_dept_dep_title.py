# Generated by Django 4.1 on 2023-02-04 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0006_remove_add_course_id_alter_add_course_coursecode'),
    ]

    operations = [
        migrations.AddField(
            model_name='dept',
            name='dep_title',
            field=models.CharField(default='null', max_length=225),
        ),
    ]
