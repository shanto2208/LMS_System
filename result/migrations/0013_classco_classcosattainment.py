# Generated by Django 4.1 on 2023-03-15 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0012_others_assesment_mark'),
    ]

    operations = [
        migrations.AddField(
            model_name='classco',
            name='classCosAttainment',
            field=models.FloatField(default='0', max_length=20),
        ),
    ]
