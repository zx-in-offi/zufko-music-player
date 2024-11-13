from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "App"

urlpatterns = [
    path("", views.landing_page, name="landing_page"),  # Route for the landing page
    path("songs/", views.index, name="index"),          # Route for the songs page
]

# Serve static files in development (if needed)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
