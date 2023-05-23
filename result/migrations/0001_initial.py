# Generated by Django 4.1 on 2023-03-12 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_course',
            fields=[
                ('courseName', models.CharField(max_length=250)),
                ('courseCode', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('depname', models.CharField(default='null', max_length=40)),
                ('credit', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='add_student',
            fields=[
                ('firstName', models.CharField(max_length=40)),
                ('lastName', models.CharField(max_length=40)),
                ('s_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('b_date', models.CharField(default='null', max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('p_email', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('dep', models.CharField(max_length=40)),
                ('seme', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='add_teachers',
            fields=[
                ('tfirstName', models.CharField(max_length=40)),
                ('tlastName', models.CharField(max_length=40)),
                ('t_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('tgender', models.CharField(default='null', max_length=20)),
                ('tp_email', models.CharField(max_length=90)),
                ('tphone', models.CharField(max_length=15)),
                ('tdep', models.CharField(max_length=40)),
                ('tCode', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='assesment_mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classId', models.CharField(max_length=20)),
                ('studentId', models.CharField(max_length=20)),
                ('assesmentName', models.CharField(default='null', max_length=20)),
                ('coName', models.CharField(max_length=20)),
                ('mark', models.FloatField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='classco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classId', models.CharField(max_length=200)),
                ('classCosname', models.CharField(max_length=40)),
                ('classCosmark', models.FloatField(default='0', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='classTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classTime', models.CharField(max_length=20)),
                ('labTime', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='clsRoom',
            fields=[
                ('classCode', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('classSemester', models.CharField(max_length=40)),
                ('courseCod', models.CharField(max_length=40)),
                ('coursesec', models.CharField(max_length=40)),
                ('instructor', models.CharField(max_length=40)),
                ('tClassTime', models.CharField(max_length=40)),
                ('labClassTime', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='clsStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdid', models.CharField(max_length=40)),
                ('classCod', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='copomaping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copomapingCc', models.CharField(max_length=20)),
                ('copomapingCo', models.CharField(max_length=20)),
                ('copomapingpo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='cos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co_name', models.CharField(max_length=40)),
                ('co_descriptions', models.CharField(max_length=200)),
                ('co_depname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='courseCos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseCos_id', models.CharField(max_length=200)),
                ('courseCosname', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='dept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=40)),
                ('dep_title', models.CharField(max_length=225)),
                ('dept_cradit', models.CharField(max_length=40)),
                ('dep_numberOfstudent', models.CharField(default='0', max_length=40)),
                ('dep_numberOfCourse', models.CharField(default='0', max_length=40)),
                ('dep_numberOfTeacher', models.CharField(default='0', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='duptclsRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dupclassName', models.CharField(max_length=40)),
                ('dupclassCode', models.CharField(max_length=40)),
                ('dupclassSemester', models.CharField(max_length=40)),
                ('dupcourseCod', models.CharField(max_length=40)),
                ('dupcoursesec', models.CharField(max_length=40)),
                ('dupinstructor', models.CharField(max_length=40)),
                ('duptClassTime', models.CharField(max_length=40)),
                ('duplabClassTime', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='greading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstMark', models.CharField(max_length=20)),
                ('secMark', models.CharField(max_length=20)),
                ('greadLetter', models.CharField(max_length=20)),
                ('gpa', models.CharField(default='null', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='pos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_name', models.CharField(max_length=40)),
                ('po_descriptions', models.CharField(max_length=200)),
                ('po_depname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=40)),
                ('studentamount', models.CharField(default='0', max_length=40)),
            ],
        ),
    ]