from django import template

register = template.Library()

from blog.models import Post

@register.assignment_tag
def get_posts_by_tag(tag_name=None):
    posts = list(Post.objects.filter(tags__tag__in=[tag_name], publish=True))
    return posts

