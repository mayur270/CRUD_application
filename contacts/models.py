from django.db import models
from django.core.validators import RegexValidator
import uuid

# Create your models here.
class EmployeeModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 13 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.fullname
