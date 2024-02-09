from django.db import models
from .choices import GENDER_CHOICES

# Create your models here.

class Customer(models.Model):
	name = models.CharField(max_length=100)
	gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
	age = models.PositiveSmallIntegerField()
	favorite_number = models.PositiveSmallIntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self) -> str:
		return f"{self.name}"