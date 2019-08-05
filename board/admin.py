from django.contrib import admin
from .models import BoardBase, PostContents

# Register your models here.

admin.site.register(BoardBase)
admin.site.register(PostContents)