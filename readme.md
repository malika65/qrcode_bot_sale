# Big Coupon

## Big Coupon - it is a bot that can save you money with virtual coupons. You can use Big Coupon to get discounts on all kinds of things - from food and retail to travel and services.

## This bot generates coupons that can be used in real shops and stores.

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/malika65/qrcode_bot_sale.git
$ cd qrcode_bot_sale
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv venv
$ ./venv/Scripts/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/`.

If everything is ok you will not see any errors

## Migration

Lets greate our tables in database:
        `python manage.py migrate`

## Telegram

Now go to the telegram and find @BotFather. Here you need create a bot and get its token. Then put this token into the settings in main file


## Webhooks

Next step is setting webhooks:
    Open ngrok, if you do not have install it : https://ngrok.com/download
    After you need run it and write following command:
                     `ngrok http 8000`
    Ngrok will give you links. Copy link with https protocol. Ngrok will get all requests from bot and receive it to you.
    To set up webhooks you need to go to the browser and put this link there. At the end you need to put tou ngrok link.
     
    [https://api.telegram.org/bot2063722420:AAEenPwY039CzQNLgO-mFmG2IDuDhGLU0Is/setWebhook?url=YOUR_NGROK_LINK]

After this steps bot should work.

For administrating your bot go to  `http://127.0.0.1:8000/` and create objects for your models.

[Documentation for code](https://github.com/malika65/qrcode_bot_sale/tree/master/documentation)