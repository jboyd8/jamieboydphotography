from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogComment
from .forms import BlogCommentForm
from django.contrib import messages


def edit_comment(request, comment_id):
    """
    Check if the comment belongs to the user, if not they should be redirected. If the method is POST, the comment
    should be updated in the db.
    If not, this should bring up the edit form in the edit-comment.html
    """

    comment = get_object_or_404(BlogComment, pk=comment_id)

    if request.user != comment.comment_user:
        messages.error(request, 'Sorry, you cannot edit another users comment.')
        return redirect('blogs')

    if request.method == 'POST':
        form = BlogCommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully edited your comment.')
            return redirect('blogs')

    form = BlogCommentForm(instance=comment)

    context = {
        'comment': comment,
        'form': form
    }

    return render(request, 'comments/edit-comment.html', context)


def delete_comment(request, comment_id):
    """
    Allow a user to delete their own comments and remove from the db. If its not their comment they should be thrown
    and error message.
    """
    comment = get_object_or_404(BlogComment, pk=comment_id)

    if request.user == comment.comment_user:
        comment.delete()
        messages.success(request, 'You have successfully deleted your comment.')
        return redirect('blogs')
    else:
        messages.error(request, 'Sorry, you cannot delete another users comment.')
        return redirect('index')
