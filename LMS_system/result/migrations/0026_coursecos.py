# Generated by Django 4.1 on 2023-03-03 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0025_alter_clsroom_classcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='courseCos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseCos_id', models.CharField(max_length=200)),
                ('courseCosname', models.CharField(max_length=40)),
            ],
        ),
    ]