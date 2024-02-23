class FormAction():

    def __init__(self, request= '', requestMethod='', form=''):
        self.__requestMethod = requestMethod
        self.__form = form
        self.__request = request

    def getRequestMethod(self):
        return self.__requestMethod
    
    def getForm(self):
        return self.__form
    
    def getRequest(self):
        return self.__request

    def setRequestMethod(self, requestMethod):
        if requestMethod.upper() not in ['GET', 'POST']:
            raise ValueError("Invalid value for request method, must be either GET or POST")
        else:
            self.__requestMethod = requestMethod.upper()

    def setForm(self, form):
        if form is None:
            raise ValueError("Invalid value for Form, must be a valid Form")
        else:
            self.__form = form

    def setRequest(self, request):
        if request is None:
            raise ValueError("Invalid value for Request, must be a valid Request")
        else:
            self.__request = request

    def checkSendRequestMethod(self):
        if self.__request.method == self.__requestMethod :
            return True
        else :
            return False
            
    def emptyForm(self):
        form = self.__form({})
        return form

    def sendRequestDataOverForm(self):
        form = self.__form(self.__request.POST,self.__request.FILES)
        return form

    def validRequestForm(self, form):
        if form.is_valid():
            return True
        else:
            return False

    def createNewRecord(self, form):
        form.cleaned_data
        form = form.save(commit=False)
        form.created_by = self.__request.user.id
        form.Last_update_by = self.__request.user.id
        form.save()
        return True
