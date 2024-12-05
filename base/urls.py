from django.urls import path
from . import views

urlpatterns = [
        path('jobs/details/<str:pk>',views.job_description, name='job_description'),
    path('search/', views.job_search, name = 'job_search'),
]




