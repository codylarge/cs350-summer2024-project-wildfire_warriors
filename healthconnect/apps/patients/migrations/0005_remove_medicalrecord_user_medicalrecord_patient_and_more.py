# Generated by Django 5.0.7 on 2024-08-11 00:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_alter_medicalrecord_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalrecord',
            name='user',
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_records', to='patients.patient'),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='prescription',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='remedy',
            field=models.TextField(),
        ),
        migrations.RemoveField(
            model_name='patient',
            name='medical_history',
        ),
        migrations.AddField(
            model_name='patient',
            name='medical_history',
            field=models.ManyToManyField(blank=True, related_name='patients', to='patients.medicalrecord'),
        ),
    ]
