# Generated by Django 4.1 on 2023-03-15 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0016_alter_coattainment_coattainmentattainment'),
    ]

    operations = [
        migrations.CreateModel(
            name='teachersFeadback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teachersFeadbackId', models.CharField(max_length=250)),
                ('teachersId', models.CharField(max_length=250)),
                ('teachersFeadback', models.CharField(max_length=250)),
            ],
        ),
    ]