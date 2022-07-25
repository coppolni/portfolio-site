from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class SkillsPage(TemplateView):
    template_name = 'skills/myskills.html'
