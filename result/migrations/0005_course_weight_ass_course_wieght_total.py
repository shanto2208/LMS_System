# Generated by Django 4.1 on 2023-03-12 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0004_coursecos_coursecosmark'),
    ]

    operations = [
        migrations.CreateModel(
            name='course_weight_ass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wieghtClassid', models.CharField(max_length=250)),
                ('totalweight', models.FloatField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='course_wieght_total',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalClassid', models.CharField(max_length=250)),
                ('totalAsses_name', models.CharField(max_length=20)),
                ('totalCo_name', models.CharField(default='null', max_length=20)),
                ('totalpoint', models.FloatField(default='0', max_length=3)),
            ],
        ),
    ]
