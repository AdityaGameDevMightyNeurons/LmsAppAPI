# Generated by Django 4.0.6 on 2022-07-12 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lmsproj', '0002_account_firstname_account_lastname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=800)),
                ('startdate', models.DateTimeField()),
                ('enddate', models.DateTimeField()),
                ('modulename', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=800)),
                ('numberofmodules', models.IntegerField(default=1)),
                ('datecreated', models.DateTimeField(auto_now_add=True)),
                ('fistmodulename', models.CharField(default='n/a', max_length=20)),
                ('fistmoduledays', models.IntegerField(default=1)),
                ('secondmodulename', models.CharField(default='n/a', max_length=20)),
                ('secondmoduledays', models.IntegerField(default=1)),
                ('thirdmodulename', models.CharField(default='n/a', max_length=20)),
                ('thirdmoduledays', models.IntegerField(default=1)),
                ('fourthmodulename', models.CharField(default='n/a', max_length=20)),
                ('fourthmoduledays', models.IntegerField(default=1)),
                ('fifthmodulename', models.CharField(default='n/a', max_length=20)),
                ('fifthmoduledays', models.IntegerField(default=1)),
                ('sixthmodulename', models.CharField(default='n/a', max_length=20)),
                ('sixthmoduledays', models.IntegerField(default=1)),
                ('seventhmodulename', models.CharField(default='n/a', max_length=20)),
                ('seventhmoduledays', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='isStudent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='isTeacher',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(auto_now_add=True, verbose_name='last login'),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=800)),
                ('startdate', models.DateTimeField(auto_now_add=True)),
                ('enddate', models.DateTimeField(auto_now_add=True)),
                ('task', models.CharField(max_length=1000)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmsproj.batch')),
            ],
        ),
        migrations.CreateModel(
            name='StudentAssignedBatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmsproj.batch')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student_Object', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_Object', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=800)),
                ('examdate', models.DateTimeField()),
                ('duration', models.IntegerField(default=3)),
                ('firstquestion', models.CharField(default='n/a', max_length=800)),
                ('firstqsnoptionone', models.CharField(default='n/a', max_length=200)),
                ('firstqsnoptiontwo', models.CharField(default='n/a', max_length=200)),
                ('firstqsnoptionthree', models.CharField(default='n/a', max_length=200)),
                ('firstqsnoptionfour', models.CharField(default='n/a', max_length=200)),
                ('firstqsnAnswer', models.CharField(default='n/a', max_length=200)),
                ('secondquestion', models.CharField(default='n/a', max_length=800)),
                ('secondqsnoptionone', models.CharField(default='n/a', max_length=200)),
                ('secondqsnoptiontwo', models.CharField(default='n/a', max_length=200)),
                ('secondqsnoptionthree', models.CharField(default='n/a', max_length=200)),
                ('secondqsnoptionfour', models.CharField(default='n/a', max_length=200)),
                ('secondqsnAnswer', models.CharField(default='n/a', max_length=200)),
                ('thirdquestion', models.CharField(default='n/a', max_length=800)),
                ('thirdqsnoptionone', models.CharField(default='n/a', max_length=200)),
                ('thirdqsnoptiontwo', models.CharField(default='n/a', max_length=200)),
                ('thirdqsnoptionthree', models.CharField(default='n/a', max_length=200)),
                ('thirdqsnoptionfour', models.CharField(default='n/a', max_length=200)),
                ('thirdqsnAnswer', models.CharField(default='n/a', max_length=200)),
                ('fourthquestion', models.CharField(default='n/a', max_length=800)),
                ('fourthqsnoptionone', models.CharField(default='n/a', max_length=200)),
                ('fourthqsnoptiontwo', models.CharField(default='n/a', max_length=200)),
                ('fourthqsnoptionthree', models.CharField(default='n/a', max_length=200)),
                ('fourthqsnoptionfour', models.CharField(default='n/a', max_length=200)),
                ('fourthqsnAnswer', models.CharField(default='n/a', max_length=200)),
                ('fifthquestion', models.CharField(default='n/a', max_length=800)),
                ('fifthqsnoptionone', models.CharField(default='n/a', max_length=200)),
                ('fifthqsnoptiontwo', models.CharField(default='n/a', max_length=200)),
                ('fifthqsnoptionthree', models.CharField(default='n/a', max_length=200)),
                ('fifthqsnoptionfour', models.CharField(default='n/a', max_length=200)),
                ('fifthqsnAnswer', models.CharField(default='n/a', max_length=200)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmsproj.batch')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmsproj.courses')),
            ],
        ),
        migrations.AddField(
            model_name='courses',
            name='createdby',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='courses',
            name='fifthmoduleteacher',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='FifthModule_Teacher', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='courses',
            name='firstmoduleteacher',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='FirstModule_Teacher', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='courses',
            name='fourthmoduleteacher',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='FourthModule_Teacher', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='courses',
            name='secondmoduleteacher',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='SecondModule_Teacher', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='courses',
            name='seventhmoduleteacher',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='SeventhModule_Teacher', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='courses',
            name='sixthmoduleteacher',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='SixthModule_Teacher', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='courses',
            name='thirdmoduleteacher',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='ThirdModule_Teacher', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='batch',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmsproj.courses'),
        ),
    ]
