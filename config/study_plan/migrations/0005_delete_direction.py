# Generated by Django 4.1.7 on 2023-02-20 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study_plan', '0004_direction_education_type_alter_direction_faculty_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Direction',
        ),
    ]