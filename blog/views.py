from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Blogs


def blogs(request):
    """FILL IN THIS COMMENT"""

    display_blogs = Blogs.objects.order_by('-date_added').filter(is_published=True)

    paginator = Paginator(display_blogs, 3)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)

    context = {
        'blogs': 'active',
        'blog_posts': paged_blogs
    }
    return render(request, 'blog/blogs.html', context)


def blog(request, blog_id):
    pass

