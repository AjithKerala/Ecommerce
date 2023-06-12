from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404

from .models import Productts,category


# Create your views here.
def Home(request):
    obj={"Value":Productts.objects.all()}

    return render(request,'Home.html',obj)

def Shops(requset):
    obj =  Productts.objects.all()
    categ=category.objects.all()
    active_category=requset.GET.get("category",'')
    if active_category:
        obj=Productts.objects.filter(category__slug=active_category)

    query=requset.GET.get('query','')
    if query:
        obj=Productts.objects.filter(Q(name__contains=query) |Q(description__contains=query))




    return render(requset,'shop.html',{"Value":obj,"cat":categ,"active_category":active_category})

def product(request,slug):
    product=get_object_or_404(Productts,slug=slug)
    return render(request,'products.html',{'product':product})
