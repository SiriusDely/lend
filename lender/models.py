from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify

from model_utils import Choices
from model_utils.fields import StatusField
from model_utils.managers import QueryManager
from model_utils.models import TimeStampedModel

class Item(TimeStampedModel):
	STATUS = Choices(u'yes', u'no', u'friends_only')
	owner = models.ForeignKey(User, related_name='items')
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255)
	description = models.TextField()
	status = StatusField()

	objects = models.Manager()
	public = QueryManager(status=u'yes').order_by(u'-modified')
	private = QueryManager(status=u'no').order_by(u'-modified')
	friends = QueryManager(status=u'friends_only').order_by(u'-modified')

	def __unicode__(self):
		return u'{0}'.format(self.name)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		super(Item, self).save(*args, **kwargs)