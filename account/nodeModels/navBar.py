from django.db import models
from django.utils.text import slugify
from generalNodes.nodeModels.userColumn import UserColumn


class FolderUrl(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name  

def upload_navbar(instance, image):
    imagename, imageexc = image.split('.')
    return 'Image/navbar/{}.{}'.format(instance, imageexc)

class NavBar(UserColumn):
    folder_url = models.ForeignKey(FolderUrl,on_delete=models.CASCADE,blank=False,null=False ,default=1)
    file_name = models.SlugField(null=True,blank=True)
    title = models.CharField(max_length=50)
    child_list_flag = models.BooleanField(default=False)
    parent = models.ForeignKey("self",on_delete=models.SET_NULL,null=True,blank=True)
    order_by = models.IntegerField()
    active_flag = models.BooleanField(default=True)

    def save (self,*args,**Kwargs):

        if self.file_name: 
            super(NavBar,self).save(*args,**Kwargs)
        else:    
            self.file_name = slugify(self.title)
            super(NavBar,self).save(*args,**Kwargs)

    def __str__(self) -> str:
        return self.title 
    
    class Meta:

        unique_together = (
            "parent",
            "order_by",
        )