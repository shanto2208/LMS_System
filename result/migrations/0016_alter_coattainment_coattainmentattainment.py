# Generated by Django 4.1 on 2023-03-15 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0015_alter_coattainment_coattainmentattainment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coattainment',
            name='coAttainmentAttainment',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
