from django.db import models


class Short(models.Model):
	full_url = models.URLField(max_length=250)  #it also makes URL validation
	short_url = models.CharField(max_length=50, unique=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	use_counter = models.PositiveIntegerField(default=0)  #counts usage of URL

	class Meta:
		db_table = 'url_shortener'
		ordering = ['-created_at']
		verbose_name = 'URL'

	def __str__(self):
		return self.full_url

	# #overriding save method
	# def save(self, *args, **kwargs):
	# 	#if hash is blank it is created randomly
	# 	if not self.short_url:
	# 		self.short_url = random_hash(self)
	# 	super(Short, self).save(*args, **kwargs)