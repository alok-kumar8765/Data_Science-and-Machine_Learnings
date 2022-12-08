from django import forms
from .models import Album,Photos
class AlbumForm(forms.ModelForm):
	class Meta:
		model=Album
		fields=('title','album_image','status')

class PhotoForm(forms.ModelForm):
	class Meta:
		model=Photos
		fields=('album','image','alt_text')

	def __init__(self, user, *args, **kwargs):
		super(PhotoForm, self).__init__(*args, **kwargs)
		self.fields['album'].queryset = Album.objects.filter(user=user)
