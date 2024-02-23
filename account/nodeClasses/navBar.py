from account.nodeModels.navBar import  NavBar
from innova.models import CompanyInformation
class NavBarClass:

    def __init__(self):
        pass

    def mainbar():

        data = NavBar.objects.all().filter(active_flag = True).order_by('order_by')
        bardata = data.filter(parent__isnull=True).order_by('order_by')
        childbardata = data.filter(parent__isnull=False).order_by('order_by')
        companyInformation = CompanyInformation.objects.all().order_by('order_by')

        context={
            'bardata':bardata,
            'childbardata':childbardata,
            'companyInformation':companyInformation
        }
        return context