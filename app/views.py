from django.shortcuts import render

# Create your views here.
import ast

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import apartment, User
from .models import evaluation as evaluationobj

# Create your views here.



def index(request):
    return HttpResponse("Main page!")

def apartmentview(request, loginuser, apartmentid=1):
    favorite = False
    if loginuser is not None:
        obj = User.objects.get(username=loginuser)
        if str(apartmentid) in ast.literal_eval(obj.favorite):
            favorite = True
        else:
            favorite = False
    data = apartment.objects.filter(id=apartmentid)[0]
    img_list = ast.literal_eval(data.img)
    img_index = [x for x in range(len(img_list))][1:]
    user_comment_list = []
    user_comment = evaluationobj.objects.filter(apartment_id=apartmentid)
    for x in user_comment:
        user_comment_list.append({
            'user': User.objects.get(uid=x.user_id).username,
            'commenttext': x.comment
        })
    out_data = {'name': data.name, 'price': data.price, 'information': data.information, 'facilities': data.facilities,
                'rent_includes': data.rent_includes, 'address': data.address, 'address_link': data.address_link,
                'score': data.score, 'comments': data.comments, 'img': img_list, "img_index": img_index
        , 'range': [1, 2, 3, 4, 5], 'message': False, 'loginuser': loginuser, 'favorite': favorite, "commenttext": user_comment_list}
    return render(request, 'apartment/index.html', {"data": out_data})

def apartment(request):
    return HttpResponse("Apartment page!")


def collection(request):
    if loginuser:
        user_favorites = ast.literal_eval(User.objects.get(username=loginuser).favorite)
        apartment_list = apartment.objects.filter(id__in=user_favorites)
        data_list = []
        for x in apartment_list:
            data_list.append({
                "id": str(x.id),
                "img": ast.literal_eval(x.img)[0],
                "name": x.name,
                "facilities": x.facilities,
                "rent_includes": x.rent_includes,
                "score": x.score,
                "information": x.information,
                "price": x.price,
                "range": [0, 1, 2, 3, 4]
            })
        data = {"loginuser": loginuser, "data_list": data_list}
        return render(request, 'apartment/collection.html', {"data": data})
    return render(request, 'apartment/login.html')

def collect(request):
    if loginuser is None:
        return HttpResponse(status=200, content='Not logged')
    referer = request.META['HTTP_REFERER']
    apartmentid = referer.split('/')[-2]
    obj = User.objects.get(username=loginuser)
    favorite_list = ast.literal_eval(obj.favorite)
    if apartmentid not in favorite_list:
        favorite_list.append(apartmentid)
        obj.favorite = str(favorite_list)
        obj.save()
        return HttpResponse(status=200, content="Save success")
    favorite_list.remove(apartmentid)
    obj.favorite = str(favorite_list)
    obj.save()
    return HttpResponse(status=200, content="Cancel success")

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