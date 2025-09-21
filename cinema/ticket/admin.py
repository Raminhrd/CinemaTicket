from django.contrib import admin
from ticket.models import *


class MovieAdmin(admin.ModelAdmin):
    list_display = ["name" , "price" , "score"]
    search_fields = ["name"]
    list_filter = ["genres"]

class CinemaAdmin(admin.ModelAdmin):
    list_display = ['name', 'adress']
    search_fields = ['name']


admin.site.register(Cinema, CinemaAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Sans)
admin.site.register(Ticket)
admin.site.register(Comment)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Criticism)