from django.db import models

CATEGORY_CHOICES = (
	('A', 'Academic'),
	('O', 'Others'),
)

SUB_CATEGORY_CHOICES = (
	('E', 'Event'),
	('N', 'Notice/Announcement'),
	('J', 'Job Related'),
	('H', 'Higher Studies Related'),
	('O', 'Others'),
)

class NewsItem(models.Model):
	def __unicode__(self):
		return self.heading
	class Meta:
		verbose_name_plural = "News Items"
	heading = models.CharField("Heading", max_length=255)
	pub_time = models.DateTimeField("Publication Date & Time", auto_now_add=True)
	published = models.BooleanField()
	category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
	sub_category = models.CharField(max_length=1, choices=SUB_CATEGORY_CHOICES)
	content = models.TextField(blank=True)
	attachment = models.FileField(upload_to="files/%Y/%m", blank=True)
