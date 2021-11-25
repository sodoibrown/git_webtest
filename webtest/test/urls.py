from django.conf.urls import url
from django.urls.conf import path
from . import views


urlpatterns = [
    path('print', views.test_print),
    path('googlelogin', views.test_googlelogin),
]