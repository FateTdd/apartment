import json
import ast

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import apartment, User
from .models import evaluation as evaluationobj
from .forms import User as FUser
from .forms import ChangeInfo


def checkLogin(func):
    def warpper(request, *args, **kwargs):
        if request.session.get('user', False):
            kwargs["loginuser"] = User.objects.get(uid=request.session.get('user'))
            return func(request, *args, **kwargs)
        else:
            kwargs['loginuser'] = None
            return func(request, *args, **kwargs)
    return warpper



@checkLogin
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