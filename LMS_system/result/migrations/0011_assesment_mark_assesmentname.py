# Generated by Django 4.1 on 2023-02-07 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0010_alter_assesment_mark_coname'),
    ]

    operations = [
        migrations.AddField(
            model_name='assesment_mark',
            name='assesmentName',
            field=models.CharField(default='null', max_length=20),
        ),
    ]