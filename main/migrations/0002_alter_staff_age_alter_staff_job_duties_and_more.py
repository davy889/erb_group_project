# Generated by Django 5.1.4 on 2025-01-18 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='job_duties',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='job_title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
