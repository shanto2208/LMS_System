# Generated by Django 4.1 on 2023-02-07 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0009_assesment_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assesment_mark',
            name='coName',
            field=models.CharField(max_length=20),
        ),
    ]
