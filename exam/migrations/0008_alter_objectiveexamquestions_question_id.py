# Generated by Django 4.1.7 on 2023-03-18 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_examdetails_appearence_examdetails_exam_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectiveexamquestions',
            name='question_id',
            field=models.CharField(editable=False, max_length=255, unique=True, verbose_name='Question ID'),
        ),
    ]
