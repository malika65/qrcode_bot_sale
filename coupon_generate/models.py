from django.db import models

BEAUTY  = 'BEAUTY'
HEALTH  = 'HEALTH'
CAFE = 'CAFE'
FUNNY = 'FUNNY'
STUDY   = 'STUDY' 
FITNESS = 'FITNESS'
CONCERT = 'CONCERT'
AUTO = 'AUTO'
CHILD = 'CHILD'
TRAVEL = 'TRAVEL'
GIFT = 'GIFT'
DIFFERENT = 'DIFFERENT'

CATEGORY_CHOICES = [
    (BEAUTY, 'Красота'),
    (HEALTH, 'Здоровье'),
    (CAFE, 'Рестораны и кафе'),
    (FUNNY, 'Развлечения'),
    (STUDY, 'Обучение'),
    (FITNESS, 'Фитнес'),
    (CONCERT, 'Концерты'),
    (AUTO, 'Авто'),
    (CHILD, 'Дети'),
    (TRAVEL, 'Путешествия'),
    (GIFT, 'Подарки'),
    (DIFFERENT, 'Разное'),
]

class Organization(models.Model):
    name = models.CharField(max_length=200,verbose_name='Название',null=True,blank=True)
    pic = models.ImageField(upload_to = 'images/organization', null = True, blank=True)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default=DIFFERENT,
    )
    description = models.TextField(max_length=3000,verbose_name='Описание',null=True,blank=True)

   
    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return self.name


class QRCode(models.Model):
    name = models.CharField(max_length=200,verbose_name='Название',null=True,blank=True)
    description = models.TextField(max_length=3000,verbose_name='Описание',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField('Время окончания qrкода')
    organization = models.ForeignKey(Organization,null=True,blank=True,on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'QRкод'
        verbose_name_plural = 'QRкоды'
    
    def __str__(self):
        return self.name


class Stock(models.Model):
    name = models.CharField(max_length=200,verbose_name='Название',null=True,blank=True)
    description = models.TextField(max_length=3000,verbose_name='Описание',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField('Время окончания акции')
    organization = models.ForeignKey(Organization,null=True,blank=True,on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
    
    def __str__(self):
        return self.name