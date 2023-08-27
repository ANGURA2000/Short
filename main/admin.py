from django.contrib import admin
# from .models import Contact
from .models import ContactMessage,ReportMessage

# Register your models here.
# admin.site.register(Contact)
admin.site.register(ContactMessage)
admin.site.register(ReportMessage)
