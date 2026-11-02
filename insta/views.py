from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.forms.formsets import formset_factory

from insta.forms import PostForm


def form_view(request: HttpRequest):
    if request.method == 'GET':
        form = PostForm()
        formset = formset_factory(PostForm, extra=3)
        return render(request, 'insta/form.html', {'form': form, "formset": formset})
    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        form.save()
        return redirect('/insta/form/')
        # return render(request, 'insta/form.html', {'form': form})


def index(request: HttpRequest):
    return render(request, 'insta/index.html')


def profile(request: HttpRequest):
    return render(request, 'insta/profile.html', {"text": "текст", "html": "<h3>Заголовок</h3>"})
