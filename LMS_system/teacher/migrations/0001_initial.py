# Generated by Django 4.1 on 2022-12-29 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='assesments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assid', models.CharField(max_length=20)),
                ('ass_name', models.CharField(max_length=20)),
                ('ass_point', models.CharField(max_length=3)),
            ],
        ),
    ]
