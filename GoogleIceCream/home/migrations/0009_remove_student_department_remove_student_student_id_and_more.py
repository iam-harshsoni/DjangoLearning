# Generated by Django 5.1.7 on 2025-03-12 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_studentid_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='department',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_id',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='StudentID',
        ),
    ]
