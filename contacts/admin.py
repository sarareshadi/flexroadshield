from django.contrib import admin
from .models import Contacts

class ContactsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone_number', 'message']
admin.site.register(Contacts, ContactsAdmin)
