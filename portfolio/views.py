from django.http import HttpResponse
from django.shortcuts import render
from .models import SkillData, SkillWeb, SkillOther


def home(request):
    skill_data = SkillData.objects.all()
    skill_web = SkillWeb.objects.all()
    skill_other = SkillOther.objects.all()

    return render(request, 'home.html', {
        'skill_data': skill_data,
        'skill_web': skill_web,
        'skill_other': skill_other
    })


def contact(request):
    return render(request, 'contact.html', {})
