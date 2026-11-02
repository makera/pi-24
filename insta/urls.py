from django.urls import path

from insta.views import form_view, index, profile

app_name = 'insta'
urlpatterns = [
    path('', index, name='index'),
    path('profile/', profile, name='profile'),
    path('form/', form_view, name='form')
]
