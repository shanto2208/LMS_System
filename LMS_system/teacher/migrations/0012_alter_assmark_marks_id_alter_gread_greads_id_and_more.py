# Generated by Django 4.1 on 2023-02-28 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0011_alter_wieght_total_totalpoint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assmark',
            name='markS_id',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='gread',
            name='greadS_id',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='lms_wieght',
            name='classid',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='weight_ass',
            name='wieghtClassid',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='wieght_number',
            name='class_id',
            field=models.CharField(default='null', max_length=250),
        ),
        migrations.AlterField(
            model_name='wieght_total',
            name='totalClassid',
            field=models.CharField(max_length=250),
        ),
    ]
