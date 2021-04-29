from django.contrib import admin

from .models import *


class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class StatisticAdmin(admin.ModelAdmin):
    list_display = ('id', 'lk', 'time', 'usr')
    list_display_links = ('id', 'lk', 'time', 'usr')


admin.site.register(Link, LinkAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Statistic, StatisticAdmin)
