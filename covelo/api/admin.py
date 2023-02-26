from django.contrib import admin
from .models import Bicycle, Station, CustomUser, Locker, Rental

admin.site.register(Bicycle)
admin.site.register(Station)
admin.site.register(CustomUser)
admin.site.register(Locker)
admin.site.register(Rental)
