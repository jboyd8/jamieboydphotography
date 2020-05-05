from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Blogs
from comments.models import BlogComment
from comments.forms import BlogCommentForm
from django.contrib import messages


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
    """
    Return the requested blog post and show its related comments. Pass through the comment form in order to add a
    comment to the blog post.
    """
    post = get_object_or_404(Blogs, pk=blog_id)

    blog_comments = get_object_or_404(BlogComment.objects.order_by('-date_posted').filter(
        is_published=True,
        blog_id=blog_id))

    if request.method == 'POST':
        form = BlogComment(
            comment_body=request.POST['comment_body'],
            comment_user=request.user,
            post=post
        )

        form.save()
        messages.success(request, 'Comment successfully added')
        return redirect('blog', blog_id)

    context = {
        'post': post,
        'blog_comments': blog_comments,
        'form': BlogCommentForm
    }

    return render(request, 'blog/blog.html', context)
