from django.db import models

class Business(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	established = models.DateField(null=True)
	image = models.ImageField(null=True, blank=True, upload_to="post_images")

	def __str__(self):
		return self.name
