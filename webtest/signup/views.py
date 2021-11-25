# from django.http import HttpResponse
from django.shortcuts import render
from .forms import client_sign_up_form
from .models import client

def sign_up(request):

    cuser_form = client_sign_up_form()   
    # cuser_pw_form = client_sign_up_pw()

    # if request.method == "POST":
    #     print(request.POST)
    #     # form 객체에 POST 요청으로 전달된 data를 form에 저장
    #     cuser_form = client_sign_up_form(request.POST)
    #     if cuser_form.is_valid():# form이 유효한 경우
    #         cuser_form.save()#데이터베이스에 저장
    
    context = {'cuser_form':cuser_form}   
    return render(request, 'signup/templates/signup/sign_up.html',context)

def sign_up_success(request):
    cuser_form = client_sign_up_form()
    if request.method == "POST":
        print(request.POST)
        # form 객체에 POST 요청으로 전달된 data를 form에 저장
        cuser_form = client_sign_up_form(request.POST)
        if cuser_form.is_valid():# form이 유효한 경우
            cuser_form.save()#데이터베이스에 저장
    
    context = {'cuser_form':cuser_form}
    return render(request, 'signup/templates/signup/sign_up_success.html',context)

def sign_up_failed(request):
    return render(request, 'signup/templates/signup/sign_up_failed.html')
