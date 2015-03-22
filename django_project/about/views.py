from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from smtplib import SMTPException
from home.models import Theme
from about.forms import ContactFrom


def about(request):
    theme = get_object_or_404(Theme, current_theme=True)

    if request.method == 'POST':
        form = ContactFrom(request.POST)
        if form.is_valid():
            try:
                send_mail("New questions from: %s" % form.cleaned_data.get("name"), form.cleaned_data.get("message"),
                          form.cleaned_data.get("email"), ["waseema393@gmail.com"], fail_silently=False)
                messages.success(request, "Message Sent Successfully")
            except SMTPException:
                messages.error(request, "Uh Oh! Something went wrong when trying to send your message")
            return redirect("about")
    else:
        form = ContactFrom()

    context = {
        "theme": theme,
        "form": form
    }

    return render(request, "about/contact.html", context)
