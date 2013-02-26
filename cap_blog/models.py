from django.db import models

from thumbnail_works.fields import EnhancedImageField

class Tag(models.Model):

    tag = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __unicode__(self):
        return self.tag

class Post(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    image = EnhancedImageField(
        upload_to = 'uploads',
        blank=True,
        process_source = dict(
            size='940x500', sharpen=True, upscale=False, format='JPEG'),
        thumbnails = {
            'avatar': dict(size='110x110'),
            'wide_avatar': dict(size='202x70'),
            'blog_avatar': dict(size='650x325'),
        }
    )

    body = models.TextField(blank=True, default="")
    link = models.FileField(upload_to="uploads", default="", blank=True)
    tags = models.ManyToManyField(Tag, related_name="posts")

    image_link = models.CharField(max_length=255, blank=True)
    date_time = models.CharField(max_length=255, blank=True)

    publish = models.BooleanField(default=False)

    @property
    def show_tags(self):
        return "\n".join([t.__unicode__() for t in self.tags.all()])

    def __unicode__(self):
        return "%s" % (self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('blog_post', (), {'post_slug' : self.slug} )

