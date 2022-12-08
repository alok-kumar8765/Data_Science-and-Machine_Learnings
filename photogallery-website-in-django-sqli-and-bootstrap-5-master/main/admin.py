from django.contrib import admin
from . import models
# Register your models here.
class AlbumAdmin(admin.ModelAdmin):
	list_display=('title','image_tag','user','status')
admin.site.register(models.Album,AlbumAdmin)

class PhotosAdmin(admin.ModelAdmin):
	list_display=('alt_text','image_tag','album')
admin.site.register(models.Photos,PhotosAdmin)