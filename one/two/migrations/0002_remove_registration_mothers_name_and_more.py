# Generated by Django 5.1.4 on 2025-07-25 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('two', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='mothers_name',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='purpose',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='reference',
        ),
        migrations.AlterField(
            model_name='registration',
            name='batch',
            field=models.CharField(choices=[('Shift 1', 'Shift 1 (6 hours): 06:00 AM - 12:00 PM (₹500/month)'), ('Shift 2', 'Shift 2 (6 hours): 12:00 PM - 06:00 PM (₹600/month)'), ('Shift 3', 'Shift 3 (5 hours): 06:00 PM - 11:00 PM (₹500/month)'), ('Shift 4', 'Shift 4 (12 hours): 06:00 PM - 06:00 AM (₹1000/month)'), ('Shift 1 + Shift 2', 'Shift 1 + Shift 2 (12 hours): ₹1000/month'), ('Shift 2 + Shift 3', 'Shift 2 + Shift 3 (11 hours): ₹1000/month')], max_length=50),
        ),
    ]
