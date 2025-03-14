# Generated by Django 5.1.7 on 2025-03-13 13:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_subject_marks_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_card_generated_date', models.DateField(auto_created=True)),
                ('student_rank', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentreportcard', to='home.student')),
            ],
        ),
    ]
