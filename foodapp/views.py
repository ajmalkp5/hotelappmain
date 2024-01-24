from django.shortcuts import render,redirect

from django.views.generic import View
from foodapp.models import Hotelapp
from django import forms

class Hotelappform(forms.Form):
    hotel=forms.CharField()
    foodname=forms.CharField()
    quantity=forms.IntegerField()
    special=forms.CharField()
    maxtime=forms.CharField()
    delivery=forms.CharField()
    price=forms.IntegerField()

class Hotelappview(View):

    def get(self,request,*args,**kwargs):
        qs=Hotelapp.objects.all()
        return render(request,"hotel_list.html",{"data":qs})

class Hotelappdetailview(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Hotelapp.objects.get(id=id)
        return render(request,"hotel_detail.html",{"data":qs})


class Hotelappdelete(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Hotelapp.objects.get(id=id).delete()
        return redirect("hotels-list")
    

class Hotelappcreate(View):

    def get(self,request,*args,**kwargs):
        form=Hotelappform()
        return render(request,"hotel_crte.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=Hotelappform(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            Hotelapp.objects.create(**data)
            return redirect("hotels-list")
        else:
            return render(request,"hotel_crte.html",{"form":form})


        # data={k:v for k,v in request.POST.items()}
        # data.pop("csrfmiddlewaretoken")
        # Hotelapp.objects.create(**data)
        # return redirect("hotels-list")
        
class Hotelappupdate(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        hotel_object=Hotelapp.objects.get(id=id)
        data={
            "hotel":hotel_object.hotel,
            "foodname":hotel_object.foodname,
            "quantity":hotel_object.quantity,
            "special":hotel_object.special,
            "maxtime":hotel_object.maxtime,
            "delivery":hotel_object.delivery,
            "price":hotel_object.price
        }
        form=Hotelappform(initial=data)
        return render(request,"hotel_edit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=Hotelappform(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            id=kwargs.get("pk")
            Hotelapp.objects.filter(id=id).update(**data)
            return redirect("hotels-list")
        else:
            return render(request,"hotel_edit.html",{"form":form})
