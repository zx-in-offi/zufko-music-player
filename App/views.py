from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Song

# Landing page view
def landing_page(request):
    return render(request, 'landing_page.html')

# Index view for songs
def index(request):
    paginator = Paginator(Song.objects.all(), 1)  # Change '1' to the number of songs you want per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "index.html", context)
