# Generated by Django 4.1 on 2023-03-20 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0022_remove_coattainment_coattainmentlevel'),
    ]

    operations = [
        migrations.CreateModel(
            name='classcopomaping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copomapingCc', models.CharField(max_length=20)),
                ('copomapingCo', models.CharField(max_length=20)),
                ('copomapingpo', models.CharField(max_length=20)),
            ],
        ),
    ]