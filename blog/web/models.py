from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
	title = models.CharField('Title', max_length=50)
	content = models.TextField('Content')
	created_by = models.ForeignKey(User)
	created_on = models.DateField('Created On')
	
	class Meta:
		verbose_name_plural = 'Entries'

