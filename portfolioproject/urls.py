from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('portfolio.urls'), name="home"),
    path('blog', include('blog.urls'), name="blog"),
    path('admin/', admin.site.urls),
]
