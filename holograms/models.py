from django.conf import settings
from django.db import models
from django.utils import timezone


class Client(models.Model):
	name = models.TextField()
	text = models.TextField()
	phone = models.CharField(max_length=20)
	email = models.TextField()
