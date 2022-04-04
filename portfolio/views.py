from django.http import HttpResponse
from django.shortcuts import render
from .models import SkillData, SkillWeb, SkillOther
from projects.models import Project

def home(request):
    skill_data = SkillData.objects.all()
    skill_web = SkillWeb.objects.all()
    skill_other = SkillOther.objects.all()

    projects = Project.objects.all().filter(frontpage=True)

    return render(request, 'home.html', {
        'skill_data': skill_data,
        'skill_web': skill_web,
        'skill_other': skill_other,
        'projects': projects
    })


def contact(request):
    return render(request, 'contact.html', {})
