from django.shortcuts import render , get_object_or_404
from django.http import HttpRequest, HttpResponse, Http404
from .models import Post

def post_list(request: HttpRequest) -> HttpResponse: 
    """
    Returns an HTTP response of the post list.
    
    Parameters
    ----------
    request: HttpRequest
        The request object.
    """
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    """
    Return an HTTP response of the post identified by the given id.
    
    Parameters
    ----------
    request: HttpRequest
        The request object.
    """
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    
    return render(request, 'blog/post/detail.html', {'post': post})
    
