from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
	path('',views.home,name='home'),
	path('photos/<int:album_id>',views.photos,name='photos'),
	path('accounts/signup',views.signup,name='signup'),
	path('dashboard',views.dashboard,name='dashboard'),
	path('user-albums',views.user_albums,name='user-albums'),
	path('add-album',views.add_album,name='add-album'),
	path('update-album/<int:id>',views.update_album,name='update-album'),
	path('delete-album/<int:id>',views.delete_album,name='delete-album'),
	path('photo-list/<int:album_id>',views.photo_list,name='photo_list'),
	path('delete-photo/<int:album_id>/<int:photo_id>',views.delete_photo,name='delete-photo'),
	path('add-photo/<int:album_id>',views.add_photo,name='add-photo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)