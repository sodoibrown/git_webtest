from typing import DefaultDict
from django.forms import ModelForm,TextInput,EmailInput
from django import forms
from .models import client

class client_sign_up_form(ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput(), max_length=10)
    class Meta:
        model = client
        fields = '__all__'
        style_str = """width: 350px; height: 45px;
        font-size:15px; padding: 5px;
        margin-bottom:8px;"""
        widgets = {
            'cname' : TextInput(attrs={
                'class':'form-control',
                'style': style_str,
                'placeholder':'NAME'
                }),
            'cemail' : EmailInput(attrs={
                'class':'form-control',
                'style': style_str,
                'placeholder':'EMAIL'
                }),
            'cpassword': forms.PasswordInput(attrs={
                'class':'form-control',
                'style': style_str,
                'placeholder':'PASSWORD'            
                }),
            'ccountry' : forms.Select(attrs={
                'class':'regDropDown',
                'style':'width: 364px; height: 59px; font-size:15px; padding: 5px; margin-bottom:8px;',
                'placeholder':'COUNTRY'  
                })
        }


# class client_sign_up_pw(ModelForm):
#     mf_cpassword = forms.CharField(widget=forms.PasswordInput())

#     class Meta:
#         model = cuser
#         fileds = '__all__'

# class test_form(forms.Form):
#     name = forms.CharField(max_length=20)
#     # email = forms.EmailField(max_length=120)
#     password = forms.CharField(widget=forms.PasswordInput, max_length=20)
#     password_recheck = forms.CharField(widget=forms.PasswordInput, label="pw_recheck", max_length=20)
#     country_choice=(('KOR','Korea'),('USA','United States of America'),('JPN','Japen'))
#     country = forms.ChoiceField(choices=country_choice)


#     def __str__(self):
#         return self.email

# class cuser_form(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)
#     password_recheck = forms.CharField(widget=forms.PasswordInput, label="pw_recheck")