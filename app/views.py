from django.shortcuts import render

# Create your views here.
import ast

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse("Main page!")

def apartmentview(request):
    return HttpResponse("Apartmentview page!")

def apartment(request):
    return HttpResponse("Apartment page!")


def collection(request):
    return HttpResponse("collection page!")

def collect(request):
    return HttpResponse("collect page!")

def cancelcollect(request):
    return HttpResponse("cancelcollect page!")

def login(request):
    return HttpResponse("login page!")

def logout(request):
    return HttpResponse("logout page!")

def evaluation(request):
    return HttpResponse("evaluation page!")

def evaluate(request):
    return HttpResponse("evaluate page!")

def registerview(request):
    return HttpResponse("registerview page!")

def register(request):
    return HttpResponse("register page!")


def userinfo(request):
    return HttpResponse("userinfo page!")


def changepwd(request):
    return HttpResponse("changepwd page!")

def forgetpwd(request):
    return HttpResponse("forgetpwd page!")

def search(request):
    return HttpResponse("search page!")