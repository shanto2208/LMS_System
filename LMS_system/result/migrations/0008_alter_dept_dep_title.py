# Generated by Django 4.1 on 2023-02-04 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0007_dept_dep_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dept',
            name='dep_title',
            field=models.CharField(max_length=225),
        ),
    ]
