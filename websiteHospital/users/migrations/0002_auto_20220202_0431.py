# Generated by Django 3.0.4 on 2022-02-01 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='visitingDates',
            field=models.CharField(max_length=15),
        ),
    ]
