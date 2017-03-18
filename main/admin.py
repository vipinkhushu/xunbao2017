from django.contrib import admin
from .models import player,question,message,logs

admin.site.register(player)
admin.site.register(question)
admin.site.register(message)
admin.site.register(logs)