from django.db import models
import uuid

class Registration(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)
    mothers_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    address = models.TextField()
    pic = models.ImageField(upload_to='photos/')
    aadhar_number = models.CharField(max_length=12)
    aadhar_pic = models.ImageField(upload_to='aadhar_photos/')
    batch = models.CharField(max_length=50)
    purpose = models.TextField()
    reference = models.CharField(max_length=200)

    def __str__(self):
        return self.name
