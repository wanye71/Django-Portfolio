from django.shortcuts import render
from .models import Jobs

def wayne(request):
    jobs = Jobs.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})
