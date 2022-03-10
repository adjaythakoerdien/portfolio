from django.urls import path
# from . import views
from .views import HomeView, BlogDetailView

urlpatterns = [
    # path('', views.home, name='home')
    path('', HomeView.as_view(), name="blog"),
    path('blogpost/<int:pk>', BlogDetailView.as_view(), name='blogpost'),
]