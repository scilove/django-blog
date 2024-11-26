from django.shortcuts import render , get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post

def post_list(request: HttpRequest) -> HttpResponse: 
    """
    Returns an HTTP response of the post list.
    
    Parameters
    ----------
    request: HttpRequest
        The request object.
        
    Returns
    -------
    response: HttpResponses
    """
    post_list = Post.published.all()
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request: HttpRequest, year: int, month: int, day: int, post: str) -> HttpResponse:
    """
    Return an HTTP response of the post identified by the given id.
    
    Parameters
    ----------
    request: HttpRequest
        The request object.
    """
    post = get_object_or_404(Post,
                            slug=post,
                            publish__year=year,
                            publish__month=month,
                            publish__day=day, 
                            status=Post.Status.PUBLISHED)
    
    return render(request, 'blog/post/detail.html', {'post': post})
    
