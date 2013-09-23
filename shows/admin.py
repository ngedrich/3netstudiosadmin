from django.contrib import admin
from shows.models import Category, Format, Show, Photo

class PhotoInline(admin.TabularInline):
	model = Photo
	extra = 5

class ShowAdmin(admin.ModelAdmin):
	inlines = [PhotoInline]

admin.site.register(Show, ShowAdmin)
admin.site.register(Category)
admin.site.register(Format)