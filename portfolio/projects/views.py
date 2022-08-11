from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Portfolio(TemplateView):
    template_name = 'projects/portfolio.html'

class ScoutGirl(TemplateView):
    template_name = 'projects/scout-girl-report.html'

class StarSocial(TemplateView):
    template_name = 'projects/star-social.html'

class SingleBlog(TemplateView):
    template_name = 'projects/single-user-blog.html'

class CollegeDash(TemplateView):
    template_name = 'projects/college-dashboard.html'

class TeamBlog(TemplateView):
    template_name = 'projects/prospects-blog.html'
