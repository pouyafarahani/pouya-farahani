from django.urls import path

from .contact_me import contact_me_form

app_name = 'about'

urlpatterns = [
    path('', contact_me_form, name='about'),
]
