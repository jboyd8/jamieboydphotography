from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Blogs


def blogs(request):
    """Create blogs view. Pick up all blog posts and display in order of most recent.
    Add pagination to amount of posts per page."""

    display_blogs = Blogs.objects.order_by('-date_added').filter(is_published=True)

    paginator = Paginator(display_blogs, 9)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)

    context = {
        'blogs': 'active',
        'blog_posts': paged_blogs
    }
    return render(request, 'blog/blogs.html', context)


def blog(request, blog_id):
    post = get_object_or_404(Blogs, pk=blog_id)

    context = {
        'post': post
    }

    return render(request, 'blog/blog.html', context)
