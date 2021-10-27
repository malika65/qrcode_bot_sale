from django.db import models

# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=200,verbose_name='Название',null=True,blank=True)
    description = models.TextField(max_length=3000,verbose_name='Описание',null=True,blank=True)

   
    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return self.name

class QRCode(models.Model):
    name = models.CharField(max_length=200,verbose_name='Название',null=True,blank=True)
    description = models.TextField(max_length=3000,verbose_name='Описание',null=True,blank=True)
    pic = models.FileField(null=True,blank=True, upload_to='images/')
    organization = models.ForeignKey(Organization,null=True,blank=True,on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'QRкод'
        verbose_name_plural = 'QRкоды'
    
    def __str__(self):
        return self.name