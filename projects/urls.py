from django.conf.urls.static import static
from django.urls import path

from portfolioproject import settings
from . import views


urlpatterns = [
    path('', views.projects, name='projects'),
    path('/<int:project_id>/', views.project, name='project_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
