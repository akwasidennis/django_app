from django.db import models
import datetime
from django.shortcuts import reverse
from django.db.models import Count, Sum
from django.contrib.auth.models import User

def get_default_action_date():
    """ get a default value for action status; create new status if not available """
    d = Date.objects.create()
    fd = Date.objects.first()
    return fd.pk



class YearDate(models.Model):
    def date_now():
        d = str(datetime.date.today())
        dt = d[:5]+'01'+'-01'
        return dt                    #datetime.datetime.strptime(str(d), '%Y-%m-%d').strftime("%Y-%m")

    dates= models.DateField(default=date_now)

    def __str__(self):
        return f'{self.dates}'


class Color(models.Model):
    def date_now():
        d = datetime.date.today()
        return d                    #datetime.datetime.strptime(str(d), '%Y-%m-%d').strftime("%Y-%m")

    color= models.CharField(max_length=20, default='#2f4f4f')
    dates= models.DateField(default=date_now)

    def __str__(self):
        return f'{self.color}'


class EachRowColor(models.Model):
    def date_now():
        d = datetime.date.today()
        return d    
    color= models.CharField(max_length=20, default='#2f4f4f')
    dates= models.DateField(default=date_now)


    def __str__(self):
        return f'{self.color}'



class Date(models.Model):
    def date_now():
        d = str(datetime.date.today())
        dt = d[:8]+'01'
        return dt                    #datetime.datetime.strptime(str(d), '%Y-%m-%d').strftime("%Y-%m")

    dates= models.DateField(default=date_now)
    eachrowcolor = models.ForeignKey(EachRowColor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.dates}'



class CommonColor(models.Model):
    def date_now():
        d = datetime.date.today()
        return d   
    color= models.CharField(max_length=20, default='#2f4f4f')
    dates= models.DateField(default=date_now)


    def __str__(self):
        return f'{self.color}'


class CheckAll(models.Model):
    def date_now():
        d = datetime.date.today()
        return d   
    check= models.CharField(max_length=20, default='none')
    dates= models.DateField(default=date_now)

    def __str__(self):
        return f'{self.check}'


class UnCheckAll(models.Model):
    def date_now():
        d = datetime.date.today()
        return d   
    uncheck= models.CharField(max_length=20, default='none')
    dates= models.DateField(default=date_now)


    def __str__(self):
        return f'{self.uncheck}'

class CheckOrUnCheck(models.Model):
    def date_now():
        d = datetime.date.today()
        return d   
    check_or_uncheck= models.CharField(max_length=20, default='none')
    dates= models.DateField(default=date_now)
    checkall = models.OneToOneField(CheckAll, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.check_or_uncheck}'


class CheckOne(models.Model):
    def date_now():
        d = datetime.date.today()
        return d   
    check_one= models.CharField(max_length=20, default='none')
    dates= models.DateField(default=date_now)


    def __str__(self):
        return f'{self.check_one}'
    
class CheckTwo(models.Model):
    def date_now():
        d = datetime.date.today()
        return d   
    check_two = models.CharField(max_length=20, default='none')
    dates= models.DateField(default=date_now)
    checkone = models.OneToOneField(CheckOne, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.check_two}'

# class CheckOnBoth(models.Model):



class Amount(models.Model):
    amount = models.FloatField()
    date_created = models.DateField(default='')
    date = models.ForeignKey(Date, on_delete=models.CASCADE)  #default=get_default_action_date,
    year_date = models.ForeignKey(YearDate, on_delete=models.CASCADE)  #default=get_default_action_date,
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    eachrowcolor = models.OneToOneField(EachRowColor, on_delete=models.CASCADE)
    checkall = models.OneToOneField(CheckAll, on_delete=models.CASCADE)
    uncheckall = models.OneToOneField(UnCheckAll, on_delete=models.CASCADE)
    checkoruncheck = models.OneToOneField(CheckOrUnCheck, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.amount}'

    @property
    def get_total(self):
        total = self.amount
        return total

    @property
    def get_month(self):
        # mnt = Amount.objects.only('amount')
        # ml = [m.date_created.strftime('%m') for m in mnt]
        # l = list(set(ml))
        # print(l)
        m = self.date_created.strftime('%m')
        return m
       
    @property
    def count_items(self):
        c = Amount.objects.count()
        if c == 1:
            return True
        else:
            return False
    
    @property
    def get_total_amount(self):
       
        amnt = Amount.objects.only('amount')
        total = sum([float(amt.get_total) for amt in amnt])
        return total

    def get_absolute_url(self):
        return reverse('my-home', kwargs={'year': self.date_created.strftime('%Y')})



