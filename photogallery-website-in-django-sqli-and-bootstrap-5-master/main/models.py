from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
# Album
class Album(models.Model):
	album_image=models.ImageField(upload_to="album_img/",null=True)
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	title=models.CharField(max_length=150)
	status=models.BooleanField(default=True)
	def __str__(self):
		return self.title

	def image_tag(self):
		return mark_safe('<img src="%s" width="80" />' % (self.album_image.url))

# PhotosModel
class Photos(models.Model):
	album=models.ForeignKey(Album, on_delete=models.CASCADE,null=True)
	image=models.ImageField(upload_to="photos/")
	alt_text=models.CharField(max_length=100)

	def __str__(self):
		return self.alt_text

	def image_tag(self):
		return mark_safe('<img src="%s" width="80" />' % (self.image.url))

