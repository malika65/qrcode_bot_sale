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
    pic = models.ImageField(upload_to = 'images/organization/', null = True, blank=True)
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

    def save(self, *args, **kwargs):
        # import inside method to prevent circular import in file
        from .views import bot
        from .buttons import get_coupon_kb
        
        # first save and before use self.id
        super(QRCode, self).save(*args, **kwargs)

        users = Subscriber.objects.all()
        for user in users:
            print(self.pk)
            bot.send_message(user.sub_id, text=f'{self.name}\n{self.description}\nДень окончания акции: {self.expiration_date.strftime("%Y-%m-%d %H:%M")}', reply_markup = get_coupon_kb(self.id))
        

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

    def save(self, *args, **kwargs):
        # import inside method to prevent circular import in file
        from .views import bot
        
        # first save and before use self.id
        super(Stock, self).save(*args, **kwargs)

        users = Subscriber.objects.all()
        for user in users:
            print(self.pk)
            bot.send_message(user.sub_id, text=f'{self.name}\n{self.description}\nДень окончания акции: {self.expiration_date.strftime("%Y-%m-%d %H:%M")}')
       
    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
    
    def __str__(self):
        return self.name




class Subscriber(models.Model):
    sub_id = models.AutoField(primary_key = True)
    username = models.CharField(max_length=200,verbose_name='Имя',null=True,blank=True)

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
    
    def __str__(self):
        return self.username