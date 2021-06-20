from django.db import models
import datetime
# Create your models here.

class Template(models.Model):
	title = models.CharField(max_length=200, default='Title')
	contents = models.TextField()
	pub_date = models.DateTimeField('date retrieved', default=datetime.datetime.now())
	def __str__(self):
		return self.title