from django.contrib import admin

from .models import Organization, QRCode, Stock, Subscriber


admin.site.register(Organization)
admin.site.register(QRCode)
admin.site.register(Stock)
admin.site.register(Subscriber)

