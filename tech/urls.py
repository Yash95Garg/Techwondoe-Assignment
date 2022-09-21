from django.urls import path
from . import views


urlpatterns = [
    path('', views.company_data),
    path('login', views.login),
    path('company/id/<str:cid>', views.companyfromID_inpath),
    path('company/id', views.companyfromID),
    path('company/name', views.companyfromName),
    path('team', views.team_data),
    path('team/create/<str:cid>', views.team_creation),
    path('team/group', views.team_data_grouped),
]