from django.contrib import admin
from .models import *

admin.site.register(Question)
admin.site.register(Options)
admin.site.register(MainQuestion)
admin.site.register(Hint)