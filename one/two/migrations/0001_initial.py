# Generated by Django 4.2.16 on 2024-10-16 15:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('fathers_name', models.CharField(max_length=100)),
                ('mothers_name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('pic', models.ImageField(upload_to='photos/')),
                ('aadhar_number', models.CharField(max_length=12)),
                ('aadhar_pic', models.ImageField(upload_to='aadhar_photos/')),
                ('batch', models.CharField(max_length=50)),
                ('purpose', models.TextField()),
                ('reference', models.CharField(max_length=200)),
            ],
        ),
    ]
