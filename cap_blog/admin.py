from django.contrib import admin

import models

class TagAdmin(admin.ModelAdmin):
    list_display = ['tag', 'slug']
    prepopulated_fields = {'slug' : ('tag',)}

    class Meta:
        model = models.Tag

class ImageInline(admin.TabularInline):
    model = models.Image

class AttributeInline(admin.TabularInline):
    model = models.Attribute

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'show_tags', 'publish']

    list_display = ['date_created', 'title', 'order', 'datetime', 'author', 'publish']
    list_editable = ['order', 'publish']

    inlines = [AttributeInline,]

    prepopulated_fields = {'slug' : ('title',)}

    def save_model(self, request, obj, form, change):
        if not change:
            try:
                obj.author = request.user
            except AttributeError:
                pass

        super(PostAdmin, self).save_model(request, obj, form, change)


    class Meta:
        model = models.Post

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag, TagAdmin)

