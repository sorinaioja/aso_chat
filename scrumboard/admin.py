from django.contrib import admin
from scrumboard.models import List,Card,Message,Room
# Register your models here.

admin.site.register(List)
admin.site.register(Card)
# Register your models here.
admin.site.register(Room)
admin.site.register(Message)