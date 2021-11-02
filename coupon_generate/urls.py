from django.urls import include,path
from coupon_generate.views import UpdateBot
from django.conf.urls import url

urlpatterns = [
    path('', UpdateBot.as_view(),name='hook'),
]