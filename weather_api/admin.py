from django.contrib import admin
from weather_api.models import City

# Register your models here.

class CityAdmin(admin.ModelAdmin):
	list_display=('city',)


admin.site.register(City, CityAdmin)


