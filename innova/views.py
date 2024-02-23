from django.urls import reverse
from django.shortcuts import render,redirect
from account.nodeClasses.navBar import NavBarClass
from django.core.paginator import Paginator
from .models import *
from .filters import *
from .forms import *
from generalNodes.nodeClasses.FormAction import *
# Create your views here.

def home(request):
    
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


def company(request):

    navdata = NavBarClass.mainbar()

    company = Company.objects.all()
    companyInformation = CompanyInformation.objects.all().order_by('order_by')

    context = {
        **navdata,
        'company':company,
        'companyInformation':companyInformation,
    }
    return render(request,'webPage/company.html',context)


def ourBoard(request):

    navdata = NavBarClass.mainbar()

    boardMember = BoardMember.objects.all().filter(active_flag=True).order_by('order_by')

    context = {
        **navdata,
        'boardMember':boardMember,
    }
    return render(request,'webPage/our-board.html',context)


def reporting(request):

    navdata = NavBarClass.mainbar()

    subTitlePharmaCovigilanceEN = SubTitlePharmaCovigilance.objects.filter(language='EN').order_by("order_by")
    subTitlePharmaCovigilanceAR = SubTitlePharmaCovigilance.objects.filter(language='AR').order_by("order_by")

    context = {
        **navdata,
        'subTitlePharmaCovigilanceEN':subTitlePharmaCovigilanceEN,
        'subTitlePharmaCovigilance':subTitlePharmaCovigilanceAR,
    }
    return render(request,'webPage/reporting.html',context)
    

def plasmaProtein(request):

    navdata = NavBarClass.mainbar()

    products = Products.objects.filter(active_flag=True,product_category__therapeutic_area=1).order_by('order_by')
    productCategory = ProductCategory.objects.all().filter(therapeutic_area=1)

    myFilter = ProductsFilter(request.POST, queryset=products)
    products = myFilter.qs

    paginator = Paginator(products, 5) # Show 4 contacts per page.
    page_number = request.POST.get('page')
    products = paginator.get_page(page_number)

    context = {
        **navdata,
        'products':products,
        'myFilter':myFilter,
        'productCategory':productCategory,
    }

    return render(request,'webPage/plasma-protein.html',context)


def applyFilter(request,category):

    products = Products.objects.filter(active_flag=True,product_category__therapeutic_area=category).order_by('order_by')
    
    myFilter = ProductsFilter(request.POST, queryset=products)
    products = myFilter.qs

    paginator = Paginator(products, 5) # Show 4 contacts per page.
    page_number = request.POST.get('page')
    products = paginator.get_page(page_number)

    context = {
        'products':products,
        'myFilter':myFilter,
    }

    return render(request,'webPage/apply-filter.html',context)


def foodSupplements(request):

    navdata = NavBarClass.mainbar()

    products = Products.objects.filter(active_flag=True,product_category__therapeutic_area=2).order_by('order_by')
    productCategory = ProductCategory.objects.all().filter(therapeutic_area=2)

    myFilter = ProductsFilter(request.POST, queryset=products)
    products = myFilter.qs

    paginator = Paginator(products, 5) # Show 4 contacts per page.
    page_number = request.POST.get('page')
    products = paginator.get_page(page_number)

    context = {
        **navdata,
        'products':products,
        'myFilter':myFilter,
        'productCategory':productCategory,
    }

    return render(request,'webPage/food-supplements.html',context)


def careers(request):

    navdata = NavBarClass.mainbar()
    career = Career.objects.all()

    form = FormAction()
    form.setRequestMethod('POST') 
    form.setForm(FormCareer)
    form.setRequest(request)

    if form.checkSendRequestMethod() :
        formdata = form.sendRequestDataOverForm()

        if form.validRequestForm(formdata):

            form.createNewRecord(formdata)
            return redirect(reverse('innova:careers'))
        
        else:
            context = {
                **navdata,
                'form':formdata,
                'career':career,
            }
        
        return render(request,'webPage/careers.html',context)

    else:
        formdata = form.emptyForm()
        context = {
                    **navdata,
                    'form':formdata,
                    'career':career,
                }
            
        return render(request,'webPage/careers.html',context)


def contact(request):

    navdata = NavBarClass.mainbar()
    contactUs = ContactUs.objects.all()

    form = FormAction()
    form.setRequestMethod('POST') 
    form.setForm(FormSuggestions)
    form.setRequest(request)

    if form.checkSendRequestMethod() :
        formdata = form.sendRequestDataOverForm()

        if form.validRequestForm(formdata):

            form.createNewRecord(formdata)
            return redirect(reverse('innova:contact'))
        
        else:
            context = {
                **navdata,
                'form':formdata,
                'contactUs':contactUs,
            }
        
        return render(request,'webPage/contact.html',context)

    else:
        formdata = form.emptyForm()
        context = {
                    **navdata,
                    'form':formdata,
                    'contactUs':contactUs,
                }
            
        return render(request,'webPage/contact.html',context)


def productDetails(request,productcategory,product):

    navdata = NavBarClass.mainbar()

    products = Products.objects.filter(name=product).order_by('order_by')
    subTitleProducts = SubTitleProducts.objects.filter(products__in=products).order_by('order_by')
    # productCategory = ProductCategory.objects.all().filter(name=productcategory)

    context = {
        **navdata,
        'products':products,
        'subTitleProducts':subTitleProducts,
        # 'productCategory':productCategory,
    }

    return render(request,'webPage/display-product.html',context)

def productDetailsFood(request,productcategory,product):

    navdata = NavBarClass.mainbar()

    products = Products.objects.filter(name=product).order_by('order_by')
    subTitleProducts = SubTitleProducts.objects.filter(products__in=products).order_by('order_by')
    # productCategory = ProductCategory.objects.all().filter(name=productcategory)

    context = {
        **navdata,
        'products':products,
        'subTitleProducts':subTitleProducts,
        # 'productCategory':productCategory,
    }

    return render(request,'webPage/display-productFood.html',context)

def patientsArea(request,product):

    navdata = NavBarClass.mainbar()

    products = Products.objects.filter(name=product).order_by('order_by')
    patientsArea = PatientsArea.objects.filter(Products__in=products).order_by('order_by')
    # productCategory = ProductCategory.objects.all().filter(name=productcategory)

    context = {
        **navdata,
        'products':products,
        'subTitleProducts':patientsArea,
        'arabic': True
        # 'productCategory':productCategory,
    }

    return render(request,'webPage/display-product.html',context)

def patientsAreaFood(request,product):

    navdata = NavBarClass.mainbar()

    products = Products.objects.filter(name=product).order_by('order_by')
    patientsArea = PatientsArea.objects.filter(Products__in=products).order_by('order_by')
    # productCategory = ProductCategory.objects.all().filter(name=productcategory)

    context = {
        **navdata,
        'products':products,
        'subTitleProducts':patientsArea,
        'arabic': True
        # 'productCategory':productCategory,
    }

    return render(request,'webPage/display-productFood.html',context)

def newsDetails(request,id):
    
    navdata = NavBarClass.mainbar()
    news = Media.objects.filter(categories=2,id=id).order_by('order_by')

    context = {
        **navdata,
        'news':news,
    }

    return render(request,'webPage/news.html',context)


def ourBoardHash(request,hash):
    
    navdata = NavBarClass.mainbar()

    boardMember = BoardMember.objects.all().filter(active_flag=True).order_by('order_by')

    context = {
        **navdata,
        'boardMember':boardMember,
        'hash':hash
    }
    return render(request,'webPage/our-board.html',context)


def companyhash(request,hash):
    
    navdata = NavBarClass.mainbar()

    company = Company.objects.all()
    companyInformation = CompanyInformation.objects.all().order_by('order_by')

    context = {
        **navdata,
        'company':company,
        'companyInformation':companyInformation,
        'hash':hash
    }
    return render(request,'webPage/company.html',context)