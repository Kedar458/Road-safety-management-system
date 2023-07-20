from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('search',views.search,name='search'),
    path('areas/<city_id>',views.areas,name='areas'),
    path('choice/<area_id>',views.choice,name='choice'),
    path('roads/<area_id>',views.roads,name='roads'),
    path('accidentss/<area_id>',views.accidentss,name='accidentss'),
    path('complaints',views.complaints,name='complaints'),
    path('report',views.report,name='report'),
    path('complaint_registered',views.complaint_registered,name='complaint_registered'),
    path('acccidents_registered',views.accidents_registered,name='accidents_registered')
]