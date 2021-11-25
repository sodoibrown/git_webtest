from django.conf.urls import url
from django.urls.conf import path
from . import views


urlpatterns = [
    path('', views.sign_up),
    path('success', views.sign_up_success),
    path('failed', views.sign_up_failed),
]