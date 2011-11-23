from models import Book, Chapter, Verse
from django.contrib import admin

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)

admin.site.register(Book, BookAdmin)
admin.site.register(Chapter)
admin.site.register(Verse)

