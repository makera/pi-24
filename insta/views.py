from django.shortcuts import render, redirect
from django.http import HttpRequest

from insta.forms import PostForm


def form_view(request: HttpRequest):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'insta/form.html', {'form': form})
    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        form.save()
        return redirect('/insta/form/')
        # return render(request, 'insta/form.html', {'form': form})
