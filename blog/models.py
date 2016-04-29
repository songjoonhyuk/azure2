from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=40)
	content = models.TextField(max_length=1000)
	image = models.ImageField()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:post_detail', args=[self.pk])


