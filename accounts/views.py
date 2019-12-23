from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import request
from rest_framework.response import Response
from .models import User
from django.contrib.auth import authenticate, logout, login


# Create your views here.

@api_view()
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = User.objects.create_user(username, password)
    user.save()
    return Response({"data": "ok"})


@api_view()
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    login(request, user)
    return Response({"data": "invalid credentials"})
