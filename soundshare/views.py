from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': "SoundShare - The Web App to Share and Rate Music!"}
    return render(request, 'soundshare/index.html', context=context_dict)


def login(request):
    context_dict = {'boldmessage': "SoundShare - The Web App to Share and Rate Music!"}
    return render(request, 'soundshare/login.html', context=context_dict)


def signup(request):
    context_dict = {'boldmessage': "SoundShare - The Web App to Share and Rate Music!"}
    return render(request, 'soundshare/signup.html', context=context_dict)


def upload(request):
    context_dict = {'boldmessage': "SoundShare - The Web App to Share and Rate Music!"}
    return render(request, 'soundshare/upload.html', context=context_dict)
