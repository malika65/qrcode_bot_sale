from django.contrib import admin

from .models import Organization, QRCode, Stock


admin.site.register(Organization)
admin.site.register(QRCode)
admin.site.register(Stock)

