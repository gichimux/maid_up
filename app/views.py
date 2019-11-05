from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def landing(request):
    return render(request, 'app/landing.html', {})


# ====================================================
# client views
# ====================================================

def client_index(request):
    return render(request, 'client/index.html', {})

def client_gig_details(request):
    return render(request, 'app/landing.html', {})

def view_client_gig(request):
    return render(request, 'app/landing.html', {})


def client_profile(request):
    return render(request, 'client/profile/profile.html', {})

# ====================================================
# freelancer views
# ====================================================

def view_worker_gig(request):
    return render(request, 'app/landing.html', {})

def worker_index(request):
    
    return render(request, 'app/landing.html', {})

def worker_gig_details(request):
    return render(request, 'app/landing.html', {})

def worker_profile(request):
    return render(request, 'app/landing.html', {})
