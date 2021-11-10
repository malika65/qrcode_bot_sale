from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from telebot import TeleBot, types
from io import BytesIO

from .buttons import category, subscribe, menu, gen_coupon_menu, get_coupon_kb
from .models import Organization, QRCode, Stock, Subscriber
from .utils import generate_qrcode

# from django.utils.timezone import datetime #important if using timezones
import datetime 

# creating Telebot instance 
bot = TeleBot(settings.TOKEN)

# Here get message from telegram and after be processed with bot
class UpdateBot(APIView):

    def post(self, request):

        json_str = request.body.decode('UTF-8')
        update = types.Update.de_json(json_str)
        bot.process_new_updates([update])
 
        return Response({'code': 200})


# decorator to react on start and help commands 
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):

    # form message that will be send
    hello_msg = '<b>Big Coupon</b> - <pre>это бот 🤖, который может сэкономить вам деньги с помощью виртуальных купонов 👨‍💻 . Вы можете использовать Big Coupon для получения 🦾 скидок от всех видов вещей - от продуктов питания и розничной торговли до поездок и услуг 💯</pre>'
    want_msg = '<i>Для получения уведомлений о новых акциях и купонах подпишитесь на нас</i>'

    bot.send_message(message.chat.id, hello_msg, parse_mode='HTML')

    bot.send_message(message.chat.id, want_msg, reply_markup=subscribe, parse_mode='HTML')



# decorator for handling callback data from buttons
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    try:
        if call.data == 'category':
            bot.send_message(call.message.chat.id,'Выберите из текущих категорий', reply_markup=category)
        
        # here we need to send all new coupons and stocks to the subscribe users 
        elif call.data == 'subscribe':
            subscribe = Subscriber.objects.create(sub_id=call.from_user.id,username=call.from_user.first_name)
            subscribe.save()

            bot.send_message(call.message.chat.id,'<pre>Спасибо за доверие 🙏. Теперь вы будете одним из первых получать уведомления о самых свежих купонах и акциях 🤑.</pre>\n\nДля того чтобы отменить подписку напишите /unsubscribe', reply_markup=menu, parse_mode='HTML')
        # callback for newest stocks and qrcodes
        elif call.data == 'fire':
            stock = Stock.objects.all()
            qrcode = QRCode.objects.all()
            
            try:
                for i in stock:
                    # check if stock experation day is nearby
                    if (i.expiration_date - datetime.timedelta(days=7)).day <= 7:
                        bot.send_message(call.message.chat.id,f'<strong>{i.name}</strong>\n<pre>{i.description}</pre>\nДата окончания акции: {i.expiration_date.strftime("%Y-%m-%d %H:%M")}', parse_mode='HTML')
            except Exception as e :
                print(e)
                bot.send_message(call.message.chat.id,'На данный момент у нас нет горящих акций, у которых срок действия неделя или меньше. Следите за обновлениями😉', parse_mode='HTML', reply_markup = menu)
            
            try:
                for j in qrcode:
                    # check if qrcode experation day is nearby
                    if (j.expiration_date - datetime.timedelta(days=7)).day <= 7:
                        bot.send_message(call.message.chat.id,f'<strong>{j.name}</strong>\n<pre>{j.description}</pre>\nДата окончания акции: {j.expiration_date.strftime("%Y-%m-%d %H:%M")}', parse_mode='HTML', reply_markup = get_coupon_kb(j.id))
            except Exception as e :
                bot.send_message(call.message.chat.id,'На данный момент у нас нет горящих акций, у которых срок действия неделя или меньше. Следите за обновлениями😉', parse_mode='HTML', reply_markup = menu)


        elif call.data.split('_')[0] == 'coupon':
            # get all coupons of specific organization found by organization_id
            coupons = QRCode.objects.filter(organization_id = call.data.split('_')[1])
            
            for i in coupons:
                bot.send_message(call.message.chat.id,f'<strong>{i.name}</strong>\n<pre>{i.description}</pre>\nДата окончания акции: {i.expiration_date.strftime("%Y-%m-%d %H:%M")}', parse_mode='HTML', reply_markup = get_coupon_kb(i.id))
                               
            bot.send_message(call.message.chat.id,'Только у нас вы найдете новейшие акции и купоны', reply_markup = menu)

        elif call.data.split('_')[0] == 'stock':
            # get stocks, found by organization id
            stocks = Stock.objects.filter(organization_id = call.data.split('_')[1])
            
            for i in stocks:
                bot.send_message(call.message.chat.id,f'<strong>{i.name}</strong>\n<pre>{i.description}</pre>\nДата окончания акции: {i.expiration_date.strftime("%Y-%m-%d %H:%M")}', parse_mode='HTML')
            
            bot.send_message(call.message.chat.id,'Только у нас вы найдете новейшие акции и купоны', reply_markup = menu)
            

        elif call.data.split('_')[0] == 'getcoupon':
            
            # get coupon by id
            coupon = QRCode.objects.filter(id = call.data.split('_')[1]).first()
            
            # forming description 
            description = f'{coupon.name},\n {coupon.description}'

            # generate qrcode
            qrcode = generate_qrcode(description)
            output = BytesIO()
            output.name = "qrcode.png"

            qrcode.save(output, format="PNG")

            # put the stream pointer back to zero before sending
            output.seek(0)
            
            # send qrcode
            bot.send_photo(call.message.chat.id, ('qrcode.png', output),caption=f'{coupon.name}\n{coupon.description}\n<strong>Ждем вас! 🎁</strong>', parse_mode='HTML')

        else :
            # get list of organization and sent their name and decription with buttons to their coupons and stocks
            organization = Organization.objects.filter(category=call.data)

            for i in organization:
                # try to send photo, if there is not so it will send photo from internet
                try:
                    bot.send_photo(call.message.chat.id, photo=i.pic,caption=f'<strong>{i.name}</strong>\n<pre>{i.description}</pre>', parse_mode='HTML', reply_markup= gen_coupon_menu(i.id))
                except BaseException as e :
                    bot.send_photo(call.message.chat.id, photo='shorturl.at/dpIKL',caption=f'<strong>{i.name}</strong>\n<pre>{i.description}</pre>', parse_mode='HTML', reply_markup= gen_coupon_menu(i.id))
            
            bot.send_message(call.message.chat.id,'Только у нас вы найдете новейшие акции и купоны', reply_markup = menu)

    except Exception as e:
        print(e)

# decorator to react on unsubscribe command
@bot.message_handler(commands=['unsubscribe'])
def send_welcome(message):
    try:
        unsubscribe = Subscriber.objects.filter(sub_id=message.chat.id)
        unsubscribe.delete()
    except BaseException as e:
        msg = "Вы не подписаны на этого бота"
        bot.send_message(message.chat.id, msg, parse_mode='HTML')
    
    msg = "Вы успешно отписались от бота."

    bot.send_message(message.chat.id, msg, parse_mode='HTML')
