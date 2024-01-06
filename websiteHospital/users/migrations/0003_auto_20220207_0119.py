# Generated by Django 3.0.4 on 2022-02-06 19:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220202_0431'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='appointment',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='patient',
            name='serial',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='category',
            field=models.CharField(choices=[('a', 'a'), ('b', 'b'), ('c', 'c')], max_length=15),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='dailyoccupation',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='visitingDates',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
