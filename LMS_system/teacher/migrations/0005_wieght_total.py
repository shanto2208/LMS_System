# Generated by Django 4.1 on 2023-02-12 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_rename_assesments_assesments_mark'),
    ]

    operations = [
        migrations.CreateModel(
            name='wieght_total',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalClassid', models.CharField(max_length=20)),
                ('totalAsses_name', models.CharField(max_length=20)),
                ('totalCo_name', models.CharField(default='null', max_length=20)),
                ('totalpoint', models.FloatField(max_length=3)),
            ],
        ),
    ]
