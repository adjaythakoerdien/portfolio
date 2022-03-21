from django.contrib import admin
from .models import SkillData, SkillWeb, SkillOther, Intro

admin.site.register(Intro)
admin.site.register(SkillData)
admin.site.register(SkillWeb)
admin.site.register(SkillOther)
