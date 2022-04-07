from django.conf.urls.static import static
from django.urls import include, path
from django.contrib import admin

from portfolioproject import settings

urlpatterns = [
    path('', include('portfolio.urls'), name="home"),
    path('blog', include('blog.urls'), name="blog"),
    path('projects', include('projects.urls'), name="projects"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
