import calendar
from myfirstapp.models import Date, Amount
from django.db.models import Count, Sum
import calendar
from django import template


register = template.Library()

@register.filter
def month_name(month_number):
    return calendar.month_name[month_number]


@register.simple_tag
def month_number(y, m):
    y = int(y)
    m = int(m)
    a = Amount.objects.order_by('date_created').filter(date_created__year=y).filter(date_created__month=m).aggregate(Sum('amount')).get('amount__sum'),
    return a[0]


@register.simple_tag
def count_items(y, m):
    y = int(y)
    m = int(m)
    a = Amount.objects.filter(date_created__year=y).filter(date_created__month=m).count()
    return a


@register.simple_tag
def each_month_cal(year, month):
    year = int(year)
    month = int(month)
    cal = calendar.HTMLCalendar().formatmonth(year, month)
    return cal


@register.simple_tag
def recorded_days_activity_cal(y, m):
    y = int(y)
    m = int(m)
    
    am = Amount.objects.order_by('date_created').filter(date_created__year=y).filter(date_created__month=m)
        
    day_from_data = []
    for a in am:
        d = a.date_created.strftime('%d')
        day_from_data.append(str(int(d)))
    
    
    c = calendar.TextCalendar(calendar.SUNDAY)
    day_from_calendar = []
    for i in c.itermonthdays(y, m):
        day_from_calendar.append(str(i))
        if i == 0:
            day_from_calendar.remove(str(i))

    _in = []
    _not = []
    
    for i in day_from_calendar:
        if i in day_from_data:
            _in.append(int(i))
        else:
            _not.append(int(i))
    return str(_in).replace('[','').replace(']','').replace(',', '')  # recorded days


@register.simple_tag
def unrecorded_days_activity_cal(y, m):
    y = int(y)
    m = int(m)
    
    am = Amount.objects.order_by('date_created').filter(date_created__year=y).filter(date_created__month=m)
        
    day_from_data = []
    for a in am:
        d = a.date_created.strftime('%d')
        day_from_data.append(str(int(d)))
    
    
    
    c = calendar.TextCalendar(calendar.SUNDAY)
    day_from_calendar = []
    for i in c.itermonthdays(y, m):
        day_from_calendar.append(str(i))
        if i == 0:
            day_from_calendar.remove(str(i))
    
    _in = []
    _not = []
    
    for i in day_from_calendar:
        if i in day_from_data:
            _in.append(int(i))
        else:
            _not.append(int(i))
    return str(_not).replace('[','').replace(']','').replace(',', '')   # unrecorded days


@register.simple_tag
def recorded_days_length(y, m):
    y = int(y)
    m = int(m)
    
    am = Amount.objects.order_by('date_created').filter(date_created__year=y).filter(date_created__month=m)
        
    day_from_data = []
    for a in am:
        d = a.date_created.strftime('%d')
        day_from_data.append(str(int(d)))
    
    
    c = calendar.TextCalendar(calendar.SUNDAY)
    day_from_calendar = []
    for i in c.itermonthdays(y, m):
        day_from_calendar.append(str(i))
        if i == 0:
            day_from_calendar.remove(str(i))

    _in = []
    _not = []
    
    for i in day_from_calendar:
        if i in day_from_data:
            _in.append(int(i))
        else:
            _not.append(int(i))
    return len(_in)  # recorded days

