# Generated by Django 5.0 on 2023-12-30 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('MATRICULE', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('NOM', models.CharField(max_length=30)),
                ('PRENOM', models.CharField(max_length=30)),
                ('SALAIRE_MENSUEL', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Payements',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('DATE', models.DateField()),
                ('MONTANT', models.FloatField()),
                ('MATRICULE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Emp_sys.employee')),
            ],
        ),
    ]
