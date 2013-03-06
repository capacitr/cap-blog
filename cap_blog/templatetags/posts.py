from django import template

register = template.Library()

from cap_blog.models import Post

@register.assignment_tag
def get_posts_by_tag(tag_name=None):
    posts = list(Post.objects.filter(tags__tag__in=[tag_name], publish=True))
    return posts

@register.assignment_tag
def get_posts(post_types=None):
    post_types = post_types.split(",")
    posts = list(Post.objects.filter(post_type__in=post_types, publish=True))
    return posts 


@register.assignment_tag
def get_prev_post(tag_name=None, pk=None):
    posts = Post.objects.filter(tags__tag__in=[tag_name], publish=True)
    prev = None
    for post in posts:
        if post.pk == pk:
            return prev
        prev = post

    return None

@register.assignment_tag
def get_next_post(tag_name=None, pk=None):
    posts = Post.objects.filter(tags__tag__in=[tag_name], publish=True)
    prev = None
    for post in posts:
        if prev and prev.pk == pk:
            return post
        prev = post
    return None

def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

@register.filter
def hyphenate(s, l):
    str_chunks = chunks(s, l)
    i = 0
    for chunk in str_chunks:
        try:
            if chunk[len(chunk)-1] != " " and str_chunks[i+1][0] != " ":
                str_chunks[i] = chunk + "-"
        except IndexError:
            pass

        i += 1
    str_chunks = "".join(str_chunks)
    return str_chunks

