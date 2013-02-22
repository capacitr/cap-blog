from django.shortcuts import render, get_object_or_404

import models

def get_post(req, post_slug=None):
    p = get_object_or_404(models.Post, slug=post_slug)
    return render(req, 'post.html', {'post': p})

