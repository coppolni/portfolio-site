from django.urls import path
from projects import views

app_name = 'projects'

urlpatterns = [
    path('portfolio/',views.Portfolio.as_view(),name='myportfolio'),
    path('scout-girl-report/',views.ScoutGirl.as_view(),name='scoutgirl'),
    path('star-social/',views.StarSocial.as_view(),name='starsocial'),
    path('single-user-blog/',views.SingleBlog.as_view(),name='singleblog'),
    path('college-dashboard/',views.CollegeDash.as_view(),name='collegedashboard'),
    path('prospects-blog/',views.TeamBlog.as_view(),name='prospectsblog'),
]
