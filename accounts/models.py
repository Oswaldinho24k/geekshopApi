from django.db import models
from django.auth.contrib.models import User
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User)
	
	