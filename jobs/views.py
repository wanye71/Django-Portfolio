from django.shortcuts import render
from .models import Jobs

def wayne(request):
    jobs = Jobs.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def detail(request, job_id):
    print(job_id)
    return render(request, 'jobs/home.html')