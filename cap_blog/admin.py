from django.contrib import admin

import models

class TagAdmin(admin.ModelAdmin):
    list_display = ['tag', 'slug']
    prepopulated_fields = {'slug' : ('tag',)}

    class Meta:
        model = models.Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'show_tags', 'publish']
    prepopulated_fields = {'slug' : ('title',)}

    class Meta:
        model = models.Post

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag, TagAdmin)

