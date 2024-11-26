from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def index(request):
    Student = {
        'st1':{
            'name':'Bijay Tamang',
            'Roll':1
        },
        'st2':{
            'name':'Anu Gurung',
            'Roll':2
        },
        'st3':{
            'name':'Alina Gurung',
            'Roll':3
        }
    }
    stu = {
        'student':Student
    }
    return render(request, 'main/index.html',context=stu)

#return render(requst, template_name, context= dictionary_name, contenttype=MIME_TYPE, status=None,using=none) 