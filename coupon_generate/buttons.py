from telebot import types


kb = [
[
    types.InlineKeyboardButton('🦋 Красота',callback_data='BEAUTY'),
    types.InlineKeyboardButton('👨‍⚕️ Здоровье',callback_data='HEALTH'),
],
[
    types.InlineKeyboardButton('🍴 Рестораны и кафе',callback_data='CAFE'),
],
[  
    types.InlineKeyboardButton('🤸 Развлечения',callback_data='FUNNY'),
    types.InlineKeyboardButton('📓 Обучение',callback_data='STUDY'),
    ] ,
[
    types.InlineKeyboardButton('🚴‍♂️ Фитнес',callback_data='FITNESS'),
    types.InlineKeyboardButton('🎇 Концерты',callback_data='CONCERT'),
    
],
[
    types.InlineKeyboardButton('🚗 Авто',callback_data='AUTO'),
    types.InlineKeyboardButton('🧒 Дети',callback_data='CHILD'),
],
[
        types.InlineKeyboardButton('🚣 Путешествия',callback_data='TRAVEL'),
        types.InlineKeyboardButton('🎁 Подарки',callback_data='GIFT'),
],
[
    types.InlineKeyboardButton('😵 Разное',callback_data='DIFFERENT'),
]
]

category = types.InlineKeyboardMarkup(kb)


kb1 = [
    [
        types.InlineKeyboardButton('📒 Категории',callback_data='category'),
        types.InlineKeyboardButton('🔥 Горящие акции',callback_data='fire'),
        
        
    ],
    [types.InlineKeyboardButton('🔔 ПОДПИСАТЬСЯ 🔔',callback_data='subscribe')]
]

subscribe = types.InlineKeyboardMarkup(kb1)

kb2 = [
    [
        types.InlineKeyboardButton('📒 Категории',callback_data='category'),
        types.InlineKeyboardButton('🔥 Горящие акции',callback_data='fire'),
    ],
    
    [
            types.InlineKeyboardButton('📁 Главное меню',callback_data='category'),
        ],
]

menu = types.InlineKeyboardMarkup(kb2)



def gen_coupon_menu(organization_id):
    
    kb3 = [
        [
            types.InlineKeyboardButton('🛍️ Акции',callback_data=f'stock_{organization_id}'),
            types.InlineKeyboardButton('🎫 Купоны',callback_data=f'coupon_{organization_id}'),
        ],
        
    ]

    coupon_menu = types.InlineKeyboardMarkup(kb3)

    return coupon_menu




def get_coupon_kb(coupon_id):
    
    kb3 = [
        [
            types.InlineKeyboardButton('🎫 Получить qr код',callback_data=f'getcoupon_{coupon_id}'),
        ],
    ]

    coupon = types.InlineKeyboardMarkup(kb3)

    return coupon

