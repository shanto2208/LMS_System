# Generated by Django 4.1 on 2023-02-28 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0023_alter_semester_studentamount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_course',
            name='courseName',
            field=models.CharField(max_length=250),
        ),
    ]
