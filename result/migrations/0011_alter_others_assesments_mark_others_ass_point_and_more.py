# Generated by Django 4.1 on 2023-03-13 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0010_alter_others_assesments_mark_others_ass_point_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='others_assesments_mark',
            name='others_ass_point',
            field=models.FloatField(max_length=20),
        ),
        migrations.AlterField(
            model_name='others_course_assesments_mark',
            name='others_course_ass_point',
            field=models.FloatField(max_length=20),
        ),
    ]