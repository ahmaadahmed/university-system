# Generated by Django 4.1.7 on 2023-07-05 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university_app', '0003_alter_department_options_alter_faculty_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='Faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university_app.faculty', verbose_name='الكلية'),
        ),
    ]
