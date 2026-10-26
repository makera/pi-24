from django.urls import path

from insta.views import form_view

app_name = 'insta'
urlpatterns = [
    path('form/', form_view, name='form')
]
