# Generated by Django 4.2.11 on 2025-03-12 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_department_studentid_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_id',
        ),
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.ManyToManyField(related_name='studentID', to='home.studentid'),
        ),
    ]
