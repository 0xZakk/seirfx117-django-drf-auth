from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.artist_list, name='artist_list'),
    url(r'^artists/(?P<pk>\d+)$', views.artist_detail, name='artist_detail'),
    url(r'^artists/new$', views.artist_create, name='artist_create'),
    url(r'^artists/(?P<pk>\d+)/edit$', views.artist_edit, name='artist_edit'),
    url(r'^artists/(?P<pk>\d+)/delete$', views.artist_delete, name='artist_delete'),


    url(r'^songs$', views.song_list, name='song_list'),
    url(r'^songs/(?P<pk>\d+)$', views.song_detail, name='song_detail'),
    url(r'^songs/new$', views.song_create, name='song_create'),
    url(r'^songs/(?P<pk>\d+)/edit$', views.song_edit, name='song_edit'),
    url(r'^songs/(?P<pk>\d+)/delete$', views.song_delete, name='song_delete'),

    url(r'^favorites/(?P<song_id>\d+)/create$', views.add_favorite, name='add_favorite'),
    url(r'^favorites/(?P<song_id>\d+)/remove$', views.remove_favorite, name='remove_favorite')
]
