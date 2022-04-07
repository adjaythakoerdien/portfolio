from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Project


def projects(request):
    projects_all = Project.objects.all()

    return render(request, 'projects_all.html', {"projects": projects_all})


def project(request, project_id):
    project_detail = get_object_or_404(Project, pk=project_id)

    return render(request, 'project_detail.html', {'project': project_detail})
