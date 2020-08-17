from django.contrib import admin
from .models import ( Date, Amount, Color, CommonColor, 
    EachRowColor, YearDate, CheckAll, UnCheckAll, CheckOrUnCheck, CheckOne, CheckTwo)



@admin.register(Date)
class DateAdmin(admin.ModelAdmin):
    list_display = ['dates']

@admin.register(YearDate)
class YearDateAdmin(admin.ModelAdmin):
    list_display = ['dates']

@admin.register(Amount)
class AmountAdmin(admin.ModelAdmin):
    list_display = ['amount', 'date_created']
    

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['color']


@admin.register(CheckAll)
class CheckAllAdmin(admin.ModelAdmin):
    list_display = ['check']

@admin.register(UnCheckAll)
class UnCheckAllAdmin(admin.ModelAdmin):
    list_display = ['uncheck']

@admin.register(CheckOrUnCheck)
class CheckOrUnCheckAdmin(admin.ModelAdmin):
    list_display = ['check_or_uncheck']


@admin.register(EachRowColor)
class EachRowColorAdmin(admin.ModelAdmin):
    list_display = ['color']


@admin.register(CommonColor)
class CommonColorAdmin(admin.ModelAdmin):
    list_display = ['color']
    

@admin.register(CheckOne)
class CheckOneAdmin(admin.ModelAdmin):
    list_display = ['check_one']


@admin.register(CheckTwo)
class CheckTwoAdmin(admin.ModelAdmin):
    list_display = ['check_two']

    
admin.site.site_header = 'Record Keeper'
