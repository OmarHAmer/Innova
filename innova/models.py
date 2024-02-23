from django.db import models
from generalNodes.nodeModels.userColumn import UserColumn
# Create your models here.


Categories = ((1, 'Slide'), (2, 'News'))

def upload_image(instance, image):
    imagename, imageexc = image.split('.')
    return 'Image/{}.{}'.format(instance, imageexc)

def upload_logo(instance, image):
    imagename, imageexc = image.split('.')
    return 'Image/logo/{}.{}'.format(instance, imageexc)

def upload_cv(instance, image):
    imagename, imageexc = image.split('.')
    return 'cv/{}.{}'.format(instance, imageexc)

class Media(UserColumn):
    subject = models.CharField(max_length=200,blank=False,null=False)
    content = models.TextField(blank=False,null=False)
    image = models.ImageField(upload_to=upload_image) 
    categories = models.IntegerField(choices=Categories)
    order_by = models.IntegerField()
    active_flag = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.subject

class Company(UserColumn):
    name = models.CharField(max_length=200,blank=False,null=False)
    description = models.TextField(blank=False,null=False)
    Image = models.ImageField(upload_to=upload_image)
    Information_subject = models.TextField(blank=False,null=False)

    def __str__(self) -> str:
        return self.name

class CompanyInformation(UserColumn):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,blank=False,null=False)
    description = models.TextField(blank=False,null=False)
    Image = models.ImageField(upload_to=upload_image,null=True)
    order_by = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class TherapeuticAreas(UserColumn):
    name = models.CharField(max_length=200,blank=False,null=False)
    description = models.TextField(blank=False,null=False)
    Image = models.ImageField(upload_to=upload_image)

    def __str__(self) -> str:
        return self.name

class ProductCategory(UserColumn):
    therapeutic_area = models.ForeignKey(TherapeuticAreas,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,blank=False,null=False)
    description = models.TextField(blank=False,null=False)

    def __str__(self) -> str:
        return self.name

class Products(UserColumn):
    product_category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,blank=False,null=False)
    description = models.TextField(blank=False,null=False)
    Image = models.ImageField(upload_to=upload_image)
    order_by = models.IntegerField()
    active_flag = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class SubTitleProducts(UserColumn):
    products = models.ForeignKey(Products,on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    description = models.TextField(blank=False,null=False)
    Image = models.ImageField(upload_to=upload_image,null=True,blank=True)
    order_by = models.IntegerField()
    active_flag = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.subject


class PatientsArea(UserColumn):
    Products = models.ForeignKey(Products,on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    description = models.TextField(blank=False,null=False)
    Image = models.ImageField(upload_to=upload_image,null=True,blank=True)
    order_by = models.IntegerField()
    active_flag = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.subject
    

class Partner(UserColumn):
    name = models.CharField(max_length=200,blank=False,null=False)
    description = models.TextField(blank=False,null=False)
    Image = models.ImageField(upload_to=upload_image)
    logo = models.ImageField(upload_to=upload_logo,blank=True,null=True)
    website = models.URLField()

    def __str__(self) -> str:
        return self.name

class BoardMember(UserColumn):
    name = models.CharField(max_length=200,blank=False,null=False)
    Position = models.CharField(max_length=200,blank=False,null=False)
    description = models.TextField(blank=False,null=False)
    Image = models.ImageField(upload_to=upload_image)
    order_by = models.IntegerField()
    active_flag = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

class ContactUs(UserColumn):
    address  = models.CharField(max_length=300,blank=False,null=False)
    country = models.CharField(max_length=100,blank=False,null=False)
    city = models.CharField(max_length=100,blank=False,null=False)
    email = models.EmailField()
    Phone = models.IntegerField()
    Fax = models.IntegerField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.address


class Suggestions(UserColumn):
    Full_Name = models.CharField(max_length=300,blank=False,null=False)
    Email_address = models.EmailField()
    Phone = models.IntegerField()
    Message = models.TextField()

    def __str__(self) -> str:
        return self.Full_Name



class PharmaCovigilance(UserColumn):
    subject = models.CharField(max_length=200,blank=False,null=False)
    description = models.TextField(blank=False,null=False)
    Image = models.ImageField(upload_to=upload_image,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    telephone = models.IntegerField(null=True,blank=True)

    def __str__(self) -> str:
        return self.subject
    

get_language = [
    ("AR", "Arabic"),
    ("EN", "English"),
]

class SubTitlePharmaCovigilance(UserColumn):
    
    pharmaCovigilance = models.ForeignKey(PharmaCovigilance,on_delete=models.CASCADE)
    subject = models.CharField(max_length=200,blank=False,null=False)
    description = models.TextField(blank=False,null=False)
    Image = models.ImageField(upload_to=upload_image,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    telephone = models.IntegerField(null=True,blank=True)
    language = models.CharField(max_length=3, choices=get_language)
    order_by = models.IntegerField()

    def __str__(self) -> str:
        return self.subject

class Career(UserColumn):
    name  = models.CharField(max_length=300,blank=False,null=False)
    telephone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=100,blank=False,null=False)
    state = models.CharField(max_length=100,blank=False,null=False)
    city = models.CharField(max_length=100,blank=False,null=False)
    jobVacancy = models.CharField(max_length=100,blank=False,null=False)
    attachCV = models.FileField(upload_to=upload_cv)

    def __str__(self) -> str:
        return self.name
    