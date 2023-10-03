from django.contrib import admin

from .models import *


# Register your models here.



class CountriesAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Name')
    list_display_links = ('Id', 'Name')
    search_fields = ('Id', 'Name')


class CurrenciesAdmin(admin.ModelAdmin):
    list_display = ('Id', 'label', 'shortlabel', 'description', 'walletnumber', 'imageurl')
    list_display_links = ('Id', 'label', 'shortlabel', 'description', 'walletnumber', 'imageurl')
    search_fields = ('Id', 'label', 'shortlabel')


class CurrencyCountryAdmin(admin.ModelAdmin):
    list_display = ('display_countries', 'display_currencies')

    def display_countries(self, obj):
        return ", ".join([country.Name for country in obj.countriesid.all()])

    def display_currencies(self, obj):
        return ", ".join([currency.shortlabel for currency in obj.currencyid.all()])

    display_countries.short_description = 'Countries'
    display_currencies.short_description = 'Currencies'



admin.site.register(Countries, CountriesAdmin)
admin.site.register(Currencies, CurrenciesAdmin)
admin.site.register(Currencycountry, CurrencyCountryAdmin)

