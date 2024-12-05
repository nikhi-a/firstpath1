from django.shortcuts import render
from django.http import HttpResponse
from .models import Job
from .search_form import JobSearchForm

# Create your views here.

def job_search(request):

    jobs = Job.objects.all()  # Default :  retrieve all jobs
    form = JobSearchForm(request.POST or None) 
    #jobs = None
    #checking if data satisfies the search criteria
    if request.method == 'POST' and form.is_valid():
        #Filter jobs based on search criteria

        title = form.cleaned_data.get('title')  
        location = form.cleaned_data.get('location')
        
        #filtering by title
        if title:
            jobs = jobs.filter(jobtitle__icontains=title) #case-insenitive title search

        #filtering by location 
        if location:
            jobs = jobs.filter(location__icontains = location) #case-insensitive location search  complocation

    return render(request, 'base/job_search.html', {'form': form, 'jobs': jobs})

def job_description(request,pk):
    #retrieve job object by id (pk) from database
    job1 = Job.objects.get(id=pk)
    #creating a dictionary to store the job object as context for the template
    context = {'job1': job1}
    #render the job description HTML template with the job object as context
    return render(request,'base/job_description.html', context)