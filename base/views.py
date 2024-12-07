from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Job, Company
from .search_form import JobSearchForm
from .forms import CompanyForm  
from django.contrib.auth.decorators import login_required

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

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'base/company_list.html', {'companies': companies})

def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'base/company_detail.html', {'company': company})

@login_required
def company_create(request):
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            company.created_by = request.user
            company.save()
            return redirect('base/company_detail', pk=company.pk)
    else:
        form = CompanyForm()
    return render(request, 'base/company_form.html', {'form': form})

@login_required
def company_edit(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect('base/company_detail', pk=company.pk)
    else:
        form = CompanyForm(instance=company)
    return render(request, 'base/company_form.html', {'form': form})

def custom_login(request):
    return render(request, 'login.html')