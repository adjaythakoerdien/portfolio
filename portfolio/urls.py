from django.conf.urls.static import static
from django.urls import path

from portfolioproject import settings
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)