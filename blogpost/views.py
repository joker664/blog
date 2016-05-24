from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render_to_response

from blogpost.models import Blogpost


def index(request):
    return render_to_response('index.html', {
        'posts': Blogpost.objects.all()[:5]
    })


def view_post(request, slug):
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blogpost, slug=slug)
    })