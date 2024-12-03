from django.contrib import admin
from .models import*

admin.site.register(Podcast)
admin.site.register(Singer)
admin.site.register(SingerFavorite)
admin.site.register(Category)
admin.site.register(PodcastFavorite)
admin.site.register(PodcastSave)
admin.site.register(PlayList)
