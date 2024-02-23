from django.urls import path
from . import views

app_name = 'innova'


urlpatterns = [

    path('',views.home,name='Home'),
    path('company',views.company,name='company'),
    path('our-board',views.ourBoard,name='our-board'),
    path('reporting',views.reporting,name='reporting'),
    path('plasma-protein',views.plasmaProtein,name='plasma-protein'),
    path('food-supplements',views.foodSupplements,name='food-supplements'),
    path('careers',views.careers,name='careers'),
    path('contact',views.contact,name='contact'),
    path('applyFilter/<int:category>',views.applyFilter,name='applyFilter'),

    path('ProductDetails/<str:productcategory>/<str:product>',views.productDetails,name='productDetails'),
    path('ProductDetails/<str:product>',views.patientsArea,name='patientsArea'),

    path('productDetailsFood/<str:productcategory>/<str:product>',views.productDetailsFood,name='productDetailsFood'),
    path('productDetailsFood/<str:product>',views.patientsAreaFood,name='patientsAreaFood'),

    path('News/<int:id>',views.newsDetails,name='newsDetails'),
    path('Ourboard/<int:hash>',views.ourBoardHash,name='ourboardhash'),
    path('Company/<int:hash>',views.companyhash,name='companyhash'),

]