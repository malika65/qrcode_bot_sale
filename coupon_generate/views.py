from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from telebot import TeleBot, types


bot = TeleBot(settings.TOKEN)

class UpdateBot(APIView):

    def post(self, request):
        # Сюда должны получать сообщения от телеграм и далее обрабатываться ботом
        json_str = request.body.decode('UTF-8')
        update = types.Update.de_json(json_str)
        bot.process_new_updates([update])
 
        return Response({'code': 200})



@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    
    bot.send_message(message.chat.id, "Здравствуй")
    