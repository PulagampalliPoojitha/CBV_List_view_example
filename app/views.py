from django.shortcuts import render
from django.views.generic import ListView
from app.models import *
# Create your views here.
class Trainers_List(ListView):
    model=Trainer
    template_name='Trainers_List.html'
    context_object_name='tl'
    ordering=['Trainer_name']

    
