from django.db import models
import uuid
import os

SHIFT_CHOICES = [
    ('Shift 1', 'Shift 1 (6 hours): 06:00 AM - 12:00 PM (₹500/month)'),
    ('Shift 2', 'Shift 2 (6 hours): 12:00 PM - 06:00 PM (₹600/month)'),
    ('Shift 3', 'Shift 3 (5 hours): 06:00 PM - 11:00 PM (₹500/month)'),
    ('Shift 4', 'Shift 4 (12 hours): 06:00 PM - 06:00 AM (₹1000/month)'),
    ('Shift 1 + Shift 2', 'Shift 1 + Shift 2 (12 hours): ₹1000/month'),
    ('Shift 2 + Shift 3', 'Shift 2 + Shift 3 (11 hours): ₹1000/month'),
]

def photo_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.aadhar_number}_photo.{ext}"
    return os.path.join('photos', filename)

def aadhar_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.aadhar_number}_aadhar.{ext}"
    return os.path.join('aadhar_photos', filename)

from django.contrib.auth.models import User

class Registration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    address = models.TextField()
    pic = models.ImageField(upload_to=photo_upload_path)
    aadhar_number = models.CharField(max_length=12)
    aadhar_pic = models.ImageField(upload_to=aadhar_upload_path)
    batch = models.CharField(max_length=50, choices=SHIFT_CHOICES)
    seat_number = models.CharField(max_length=20, blank=True, null=True, default='N/A')

    def __str__(self):
        return self.name
