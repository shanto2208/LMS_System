# Generated by Django 4.1 on 2023-02-28 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0010_gread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wieght_total',
            name='totalpoint',
            field=models.FloatField(default='0', max_length=3),
        ),
    ]
