from django.http import HttpResponse
from django.shortcuts import render
from .models import Project


def projects(request):
    projects_all = Project.objects.all()

    return render(request, 'projects_all.html', {"projects": projects_all})
