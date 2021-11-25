from django.http import HttpResponse
from django.shortcuts import render
from .models import cuser,fuser
from django.db import connection

# Create your views here.

# def test_print(request):
#     list_test = cuser.objects.all()
#     return render(request, 'test/templates/test/test_print.html',{'list_test':list_test})

def test_print(request):
    list_ctest = cuser.objects.all()
    list_ftest = fuser

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Freelance_User")
    rst = cursor.fetchall()

    return render(request, 'test/templates/test/test_print.html',
    {'list_ftest':list_ftest, 'list_ctest':list_ctest,
    'rst':rst})

def test_googlelogin(request):
    return render(request, 'test/templates/test/test_googlelogin.html')