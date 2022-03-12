from django.urls import path
# from . import views
from .views import HomeView, BlogDetailView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('', views.home, name='home')
    path('', HomeView.as_view(), name="blog"),
    path('blogpost/<int:pk>', BlogDetailView.as_view(), name='blogpost'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
