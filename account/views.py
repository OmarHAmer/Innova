from django.urls import reverse
from django.shortcuts import render,redirect
from account.nodeClasses.navBar import NavBarClass
from innova.models import *
# Create your views here.

def redirectHome(request):
    return redirect(reverse('innova:Home'))

def navpage(request,app,slug):


    if 'Home' in slug :
        navdata = NavBarClass.mainbar()

        media = Media.objects.all()
        slideData = media.filter(categories=1,active_flag=True).order_by('order_by')
        newsData = media.filter(categories=2,active_flag=True).order_by('order_by')

        partnerData = Partner.objects.all()
        boardMember = BoardMember.objects.all().filter(active_flag=True).order_by('order_by')
        products = Products.objects.all().filter(active_flag=True).order_by('order_by')

        context = {
            **navdata,
            'slideData':slideData,
            'newsData':newsData,
            'partnerData':partnerData,
            'boardMember':boardMember,
            'products':products,
        }
        return render(request,'webPage/Home.html',context)

    navdata = NavBarClass.mainbar()
    context = {
        **navdata
    }

    if app == 'None' :
        return render(request,slug+'.html',context)
    else:
        return render(request,app+'/'+slug+'.html',context)