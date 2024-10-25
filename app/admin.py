from django.contrib import admin
from .models import *
from django.utils.html import format_html

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'cover_image_tag')

    def cover_image_tag(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.cover_image.url))
        return "No Image"

    cover_image_tag.short_description = 'Main Image'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'cover_image_tag')

    def cover_image_tag(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.cover_image.url))
        return "No Image"

    cover_image_tag.short_description = 'Main Image'

admin.site.register(Project, ProjectAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.register(AdditionalProjectImage)
admin.site.register(AdditionalProductImage)
