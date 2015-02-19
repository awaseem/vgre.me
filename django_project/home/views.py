from django.shortcuts import render, get_object_or_404
from home.models import Header


def index(request):
    current_header = get_object_or_404(Header, current_header=True)
    context = {"current_header": current_header}
    return render(request, "home/index_test.html", context)