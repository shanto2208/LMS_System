# Generated by Django 4.1 on 2023-03-15 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0014_coattainment_remove_classco_classcosattainment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coattainment',
            name='coAttainmentAttainment',
            field=models.FloatField(default='0', max_length=3),
        ),
    ]
