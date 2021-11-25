from django.db import models
from django import forms
from django.utils.regex_helper import Choice

class client(models.Model):
    cname = models.CharField(max_length=20, verbose_name='cname')
    cemail = models.EmailField(max_length=120, verbose_name='cemail')
    cpassword = models.CharField(max_length=10, verbose_name='cpassword')
    choice_country_field = (('KOR','Korea'),('USA','United State Of America'),('JPN','Japen'))
    ccountry = models.CharField(choices=choice_country_field, max_length=5, verbose_name='ccountry')

    def __str__(self):
        return self.cname

