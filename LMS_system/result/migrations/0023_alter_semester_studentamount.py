# Generated by Django 4.1 on 2023-02-28 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0022_alter_add_teachers_tp_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='studentamount',
            field=models.CharField(default='0', max_length=40),
        ),
    ]