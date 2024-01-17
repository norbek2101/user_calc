from django.contrib import admin
from .models import Usrs
from .models import Usrs, Country, Region, District, City, Place

@admin.register(Usrs)
class UsrsAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    def display_places(self, obj):
        # Assuming 'places' is the name of the many-to-many field
        return ", ".join([place for place in obj.users.all()])

    display_places.short_description = 'users'

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'country',)
    list_filter = ('country',)

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'region',)
    list_filter = ('region',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'region',)
    list_filter = ('region',)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('country', 'region', 'district', 'city',)
    list_filter = ('country', 'region', 'district', 'city',)