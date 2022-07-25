from django.urls import path
from skills import views

app_name = 'skills'

urlpatterns = [
    path('',views.SkillsPage.as_view(),name='myskills'),
]
