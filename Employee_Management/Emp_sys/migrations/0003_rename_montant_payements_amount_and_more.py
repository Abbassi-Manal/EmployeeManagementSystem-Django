# Generated by Django 5.0 on 2023-12-30 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Emp_sys', '0002_rename_prenom_employee_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payements',
            old_name='MONTANT',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='payements',
            old_name='DATE',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='payements',
            old_name='ID',
            new_name='id',
        ),
    ]
