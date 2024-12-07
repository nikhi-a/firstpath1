from django.urls import path
from . import views
from base import views

urlpatterns = [
        path('jobs/details/<str:pk>',views.job_description, name='job_description'),
        path('search/', views.job_search, name = 'job_search'),
        path('companies/', views.company_list, name='company_list'),
        path('companies/create/', views.company_create, name='company_create'),
        path('companies/<str:pk>', views.company_detail, name='company_detail'),
        path('companies/<str:pk>/edit/', views.company_edit, name='company_edit'),
        path('login/', views.custom_login, name='login'),
]




