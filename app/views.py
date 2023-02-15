from django.shortcuts import render
from .models import Student
from django.views.generic.detail import DetailView
# Create your views here.
#detail view gives single instance object this is most important features
class StudentDetailview(DetailView):
    model=Student
    template_name='app/home.html'
    #here we provide the custome template name this is the very important concept to 
