from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
import os
from .forms import ContactForm
from.models import Contact

# Created an env var for the admin email so not in code.
ADMINS_EMAIL = os.environ.get('ADMINS_EMAIL')


def contact(request):
    """Create the contact view. If the request is POST check if the user is authenticated or not and pass
    values to the contact form based on it. An email should then be sent to the admins. If not post pass through a
    blank version of the form."""

    if request.method == 'POST':
        if request.user.is_authenticated:

            form = Contact(
                contact_title=request.POST['contact_title'],
                contact_body=request.POST['contact_body'],
                email=request.POST['email'],
                query_user=request.user
            )

            form.save()

        else:
            form = Contact(
                contact_title=request.POST['contact_title'],
                contact_body=request.POST['contact_body'],
                email=request.POST['email']
            )

            form.save()

        send_mail(
            'New enquiry from JBP',
            'You have a new message. See admin panel for details.',
            os.environ.get('SITE_EMAIL'),
            [ADMINS_EMAIL],
            fail_silently=False,
        )

        messages.success(request, 'Your enquiry has been submitted, I will get back to you shortly.')

    else:
        if request.user.is_authenticated:
            form = ContactForm(
                initial={'email': request.user.email}
            )
        else:
            form = ContactForm()

        context = {
            'contact': 'active',
            'form': form
        }

    return render(request, 'contact/contact.html', context)
