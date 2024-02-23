from django.contrib import admin
from .models import *
# Register your models here.

class MediaAdmin(admin.ModelAdmin): 
    list_display = ('subject', 'categories', 'active_flag')
admin.site.register(Media,MediaAdmin)


admin.site.register(Company)
admin.site.register(CompanyInformation)
admin.site.register(TherapeuticAreas)
admin.site.register(ProductCategory)
admin.site.register(Products)

class SubTitleProductsAdmin(admin.ModelAdmin): 
    list_display = ('products', 'subject', 'active_flag')
    
admin.site.register(SubTitleProducts,SubTitleProductsAdmin)

admin.site.register(Partner)
admin.site.register(BoardMember)

class ContactUsAdmin(admin.ModelAdmin): 
    list_display = ('country', 'city', 'address','email')

admin.site.register(ContactUs,ContactUsAdmin)

class SuggestionsAdmin(admin.ModelAdmin): 
    list_display = ('Full_Name', 'Email_address', 'Phone')
admin.site.register(Suggestions,SuggestionsAdmin)

admin.site.register(PharmaCovigilance)
admin.site.register(SubTitlePharmaCovigilance)
admin.site.register(Career)

class PatientsAreaAdmin(admin.ModelAdmin): 
    list_display = ('Products', 'subject', 'active_flag')
admin.site.register(PatientsArea,PatientsAreaAdmin)
