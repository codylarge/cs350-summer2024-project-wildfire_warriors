# Generated by Django 5.0.7 on 2024-08-10 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='accepting_new_patients',
            field=models.BooleanField(default=True),
        ),
    ]
