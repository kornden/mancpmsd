

from django.shortcuts import render
from .models import Post, Doctor, Unit, Drug

def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'cpmsdblog/index.html', context)

def doctors(request):
    doctors_list = Doctor.objects.order_by('name')
    context = {'doctors_list': doctors_list}
    return render(request, 'cpmsdblog/index.html', context)

def units(request):
    unit_list = Unit.objects.order_by('name')
    context = {'unit_list': unit_list}
    return render(request, 'cpmsdblog/index.html', context)

def freedrugs(request):
    drug_list = Drug.objects.all()
    context = {'drug_list': drug_list}
    return render(request, 'cpmsdblog/index.html', context)
