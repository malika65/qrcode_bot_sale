from django.contrib import admin

from .models import Organization, QRCode


admin.site.register(Organization)
admin.site.register(QRCode)

