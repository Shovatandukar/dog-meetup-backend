from django.contrib import admin
from .models import Dog, Owner, Event

admin.site.register(Dog)
admin.site.register(Owner)
admin.site.register(Event)
