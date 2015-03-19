from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from home.models import Theme
from about.forms import ContactFrom


def about(request):
    theme = get_object_or_404(Theme, current_theme=True)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactFrom(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print form.cleaned_data
            # redirect to a new URL:
            return redirect("about")
    else:
        form = ContactFrom()

    context = {
        "theme": theme,
        "form": form
    }
    return render(request, "about/contact.html", context)
