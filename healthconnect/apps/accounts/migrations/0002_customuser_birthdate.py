# Generated by Django 5.0.7 on 2024-08-04 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
