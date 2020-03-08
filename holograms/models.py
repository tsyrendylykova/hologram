from django.conf import settings
from django.db import models
from django.utils import timezone


class Client(models.Model):
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=20)