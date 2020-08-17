from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from myfirstapp.models import Date, Amount, Color, CommonColor, EachRowColor, YearDate, CheckAll, UnCheckAll, CheckOrUnCheck, CheckOne, CheckTwo
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import datetime
import calendar
from django.contrib import messages
from django.views.generic import UpdateView
from django.db.models import Count, Sum
from .forms import AmountForm


def check_one(request, year):
    if CheckOne.objects.filter(dates__year=year).count() > 0 or CheckTwo.objects.filter(dates__year=year).count() > 0:
        #common color
        col_id = CheckOne.objects.filter(dates__year=year).first()
        print(col_id)
        red_col = 'none'
        c = CheckOne.objects.filter(dates__year=year).get(id=col_id.id)
        c.check_one = red_col
        c.save()
        # check two
        col_id2 = CheckTwo.objects.filter(dates__year=year).first()
        print(col_id2)
        red_col2 = 'block'
        c2 = CheckTwo.objects.filter(dates__year=year).get(id=col_id2.id)
        c2.check_two = red_col2
        c2.save()
    else:
        def saveCol():
            red_col = 'block'
            ck = CheckOne.objects.create(check_one='none')
            c_col = CheckTwo(check_two=red_col, checkone=ck)
            c_col.save()

        saveCol()

    if CheckAll.objects.filter(dates__year=year).count() > 0:
        ck = CheckAll.objects.filter(dates__year=year)
        print(ck)
        for obj in ck:
            obj.check = 'block'
            obj.save()
    else:   
        def saveCheck():
            row_ck = 'none'
            ck = CheckAll(ckeck=row_ck)
            ck.save()
        saveCheck()
    
    return HttpResponseRedirect(reverse('my-home', args=(year,)))


def check_two(request, year):
    if CheckTwo.objects.filter(dates__year=year).count() > 0 or CheckTwo.objects.filter(dates__year=year).count() > 0:
        #common color
        col_id = CheckOne.objects.filter(dates__year=year).first()
        print(col_id)
        red_col = 'block'
        c = CheckOne.objects.filter(dates__year=year).get(id=col_id.id)
        c.check_one = red_col
        c.save()

        #check two
        col_id2 = CheckTwo.objects.filter(dates__year=year).first()
        print(col_id2)
        red_col2 = 'none'
        c2 = CheckTwo.objects.filter(dates__year=year).get(id=col_id2.id)
        c2.check_two = red_col2
        c2.save()
    else:
        def saveCol():
            red_col = 'none'
            ck = CheckOne.objects.create(check_one='block')
            c_col = CheckTwo(check_two=red_col, checkone=ck)
            c_col.save()
        saveCol()


    if CheckAll.objects.filter(dates__year=year).count() > 0:
        ck = CheckAll.objects.filter(dates__year=year)
        print(ck)
        for obj in ck:
            obj.check = 'none'
            obj.save()
    else:   
        def saveUnCheck():
            row_ck = 'block'
            ck = CheckAll(ckeck=row_ck)
            ck.save()
        saveUnCheck()
    
    return HttpResponseRedirect(reverse('my-home', args=(year,)))



def delete_all(request, year):
    dt = Date.objects.order_by('dates').filter(dates__year=year)
    yr = YearDate.objects.order_by('dates').filter(dates__year=year)
    col = Color.objects.order_by('dates').filter(dates__year=year)
    ec = EachRowColor.objects.order_by('dates').filter(dates__year=year)
    cc = CommonColor.objects.order_by('dates').filter(dates__year=year)
    ck = CheckAll.objects.order_by('dates').filter(dates__year=year)
    uc = UnCheckAll.objects.order_by('dates').filter(dates__year=year)
    c_u = CheckOrUnCheck.objects.order_by('dates').filter(dates__year=year)
    co = CheckOne.objects.order_by('dates').filter(dates__year=year)
    ct = CheckTwo.objects.order_by('dates').filter(dates__year=year)
    for d in dt:
        d.delete()
    for y in yr:
        y.delete()
    for c in col:
        c.delete()
    for c in ec:
        c.delete()
    for c in cc:
        c.delete()
    for c in ck:
        c.delete()
    for c in uc:
        c.delete()
    for c in c_u:
        c.delete()
    for c in co:
        c.delete()
    for c in ct:
        c.delete()
    messages.success(request, 'All items deleted successfully!')


    return HttpResponseRedirect(reverse('my-home', args=(year,)))


def home(request, year):
    c_t= CheckTwo.objects.order_by('dates').filter(dates__year=year)

    for c in c_t:
        print(c)
        print(c.checkone)
        break

    context = {
        'sum': Amount.objects.order_by('date_created').filter(date_created__year=year).aggregate(Sum('amount')).get('amount__sum'),

        'dt': Date.objects.order_by('dates').filter(dates__year=year), #.values('dates').filter(dates__year=year).distinct(),
        'c_u': CheckOrUnCheck.objects.order_by('dates').filter(dates__year=year),
        'c_t': CheckTwo.objects.order_by('dates').filter(dates__year=year).first(),
        'c': EachRowColor.objects.all(),
        'amnt': Amount.objects.order_by('date_created').filter(date_created__year=year),
        'year': year,
      
    }
    return render(request, 'myfirstapp/home.html', context)



def data_calendar(request, year):
    context = {
         'amnt': Amount.objects.order_by('date_created').filter(date_created__year=year),
         'dt': YearDate.objects.order_by('dates').values('dates').distinct(),
    }
    return render(request, 'myfirstapp/data_calendar.html', context)


def year_home(request):
    
    c = calendar.HTMLCalendar(calendar.MONDAY)
    context = {
        'dt': YearDate.objects.order_by('dates').values('dates').distinct(),
        'amnt': Amount.objects.order_by('date_created').filter(date_created__year=2020),
        's': c.formatmonth(2020, 7)
    }
    return render(request, 'myfirstapp/year_home.html', context)


def month_detail(request, year, month):
    
    context = {
        'dt': Date.objects.order_by('date_created'),
        'amnt': Amount.objects.order_by('date_created').filter(date_created__year=year).filter(date_created__month=month),
        'month': month
    }
    return render(request, 'myfirstapp/month_details.html', context)


def del_item(request, pk, year):
    
    a = Amount.objects.get(id=pk)
    a.delete()
    messages.success(request, 'Item deleted successfully!')
    if Amount.objects.filter(date_created__year=year).count() == int(0):
        print('All deleted!')
        dt = Date.objects.order_by('dates').filter(dates__year=year)
        yr = YearDate.objects.order_by('dates').filter(dates__year=year)
        col = Color.objects.order_by('dates').filter(dates__year=year)
        ec = EachRowColor.objects.order_by('dates').filter(dates__year=year)
        cc = CommonColor.objects.order_by('dates').filter(dates__year=year)
        ck = CheckAll.objects.order_by('dates').filter(dates__year=year)
        uc = UnCheckAll.objects.order_by('dates').filter(dates__year=year)
        c_u = CheckOrUnCheck.objects.order_by('dates').filter(dates__year=year)
        co = CheckOne.objects.order_by('dates').filter(dates__year=year)
        ct = CheckTwo.objects.order_by('dates').filter(dates__year=year)
        for d in dt:
            d.delete()
        for y in yr:
            y.delete()
        for c in col:
            c.delete()
        for c in ec:
            c.delete()
        for c in cc:
            c.delete()
        for c in ck:
            c.delete()
        for c in uc:
            c.delete()
        for c in c_u:
            c.delete()
        for c in co:
            c.delete()
        for c in ct:
            c.delete()

    
    return HttpResponseRedirect(reverse('my-home', args=(year,)))



def save_amount(request):
   
    if request.method == 'POST':
        form = AmountForm(request.POST)
        if form.is_valid():
            col_list = ['#20124d', '#ff0000', '#3d85c6', '#434343', '#00ffff', '#4c1130', '#2f4f4f', '#ffe599', '#999999', '#134f5c', 
                        '#9900ff', '#ff00ff', '#c27ba0'
                        ]

            
            y_d = YearDate.objects.create()  # year_date object
            c = Color.objects.create(color='#2f4f4f')  # color object
            d_created = datetime.date.today()
            c_user = request.user  # user instance
            eachMonth = datetime.date.today().strftime('%m')
            amnt = form.cleaned_data.get('amount')  # amount object
            print(type(eachMonth))

            b = 'none'
            co = CheckOne.objects.create(check_one='block')
            ct = CheckTwo(check_two=b, checkone=co)
            ct.save()
            
            if eachMonth == '01':
                
                erc = EachRowColor.objects.create(color=col_list[0])  # color object
                d = Date.objects.create(eachrowcolor=erc)  # date object
                ck = CheckAll.objects.create(check='none')
                uck = UnCheckAll.objects.create(uncheck ='none')
                c_u = CheckOrUnCheck.objects.create(check_or_uncheck ='block', checkall=ck)
                data = Amount(amount=amnt, date_created=d_created, date=d, year_date=y_d, color=c, eachrowcolor=erc, checkall=ck, uncheckall=uck, checkoruncheck=c_u, author=c_user)
                data.save()
            elif eachMonth == '02':
                
                erc = EachRowColor.objects.create(color=col_list[1])  # color object
                d = Date.objects.create(eachrowcolor=erc)  # date object
                ck = CheckAll.objects.create(check='none')
                uck = UnCheckAll.objects.create(uncheck='none')
                c_u = CheckOrUnCheck.objects.create(check_or_uncheck ='block', checkall=ck)
                data = Amount(amount=amnt, date_created=d_created, date=d, year_date=y_d, color=c, eachrowcolor=erc, checkall=ck, uncheckall=uck, checkoruncheck=c_u, author=c_user)
                data.save()
            elif eachMonth == '03':
                erc = EachRowColor.objects.create(color=col_list[2])  # color object
                d = Date.objects.create(eachrowcolor=erc)  # date object
                ck = CheckAll.objects.create(check='none')
                uck = UnCheckAll.objects.create(uncheck='none')
                c_u = CheckOrUnCheck.objects.create(check_or_uncheck ='block', checkall=ck)
                data = Amount(amount=amnt, date_created=d_created, date=d, year_date=y_d, color=c, eachrowcolor=erc, checkall=ck, uncheckall=uck, checkoruncheck=c_u, author=c_user)
                data.save()
            elif eachMonth == '04':
                erc = EachRowColor.objects.create(color=col_list[3])  # color object
                d = Date.objects.create(eachrowcolor=erc)  # date object
                ck = CheckAll.objects.create(check='none')
                uck = UnCheckAll.objects.create(uncheck='none')
                c_u = CheckOrUnCheck.objects.create(check_or_uncheck ='block', checkall=ck)
                data = Amount(amount=amnt, date_created=d_created, date=d, year_date=y_d, color=c, eachrowcolor=erc, checkall=ck, uncheckall=uck, checkoruncheck=c_u, author=c_user)
                data.save()
            elif eachMonth == '05':
                erc = EachRowColor.objects.create(color=col_list[4])  # color object
                d = Date.objects.create(eachrowcolor=erc)  # date object
                ck = CheckAll.objects.create(check='none')
                uck = UnCheckAll.objects.create(uncheck='none')
                c_u = CheckOrUnCheck.objects.create(check_or_uncheck ='block', checkall=ck)
                data = Amount(amount=amnt, date_created=d_created, date=d, year_date=y_d, color=c, eachrowcolor=erc, checkall=ck, uncheckall=uck, checkoruncheck=c_u, author=c_user)
                data.save()
            elif eachMonth == '06':
                erc = EachRowColor.objects.create(color=col_list[5])  # color object
                d = Date.objects.create(eachrowcolor=erc)  # date object
                ck = CheckAll.objects.create(check='none')
                uck = UnCheckAll.objects.create(uncheck='none')
                c_u = CheckOrUnCheck.objects.create(check_or_uncheck ='block', checkall=ck)
                data = Amount(amount=amnt, date_created=d_created, date=d, year_date=y_d, color=c, eachrowcolor=erc, checkall=ck, uncheckall=uck, checkoruncheck=c_u, author=c_user)
                data.save()
            elif eachMonth == '07':
                erc = EachRowColor.objects.create(color=col_list[6])  # color object
                d = Date.objects.create(eachrowcolor=erc)  # date object
                ck = CheckAll.objects.create(check='none')
                uck = UnCheckAll.objects.create(uncheck='none')
                c_u = CheckOrUnCheck.objects.create(check_or_uncheck ='block', checkall=ck)
                data = Amount(amount=amnt, date_created=d_created, date=d, year_date=y_d, color=c, eachrowcolor=erc, checkall=ck, uncheckall=uck, checkoruncheck=c_u, author=c_user)
                data.save()
            elif eachMonth == '08':
                erc = EachRowColor.objects.create(color=col_list[7])  # color object
                d = Date.objects.create(eachrowcolor=erc)  # date object
                ck = CheckAll.objects.create(check='none')
                uck = UnCheckAll.objects.create(uncheck='none')
                c_u = CheckOrUnCheck.objects.create(check_or_uncheck ='block', checkall=ck)
                data = Amount(amount=amnt, date_created=d_created, date=d, year_date=y_d, color=c, eachrowcolor=erc, checkall=ck, uncheckall=uck, checkoruncheck=c_u, author=c_user)
                data.save()
            elif eachMonth == '09':
                erc = EachRowColor.objects.create(color=col_list[8])  # color object
                d = Date.objects.create(eachrowcolor=erc)  # date object
                ck = CheckAll.objects.create(check='none')
                uck = UnCheckAll.objects.create(uncheck='none')
                c_u = CheckOrUnCheck.objects.create(check_or_uncheck ='block', checkall=ck)
                data = Amount(amount=amnt, date_created=d_created, date=d, year_date=y_d, color=c, eachrowcolor=erc, checkall=ck, uncheckall=uck, checkoruncheck=c_u, author=c_user)
                data.save()
            elif eachMonth == '10':
                erc = EachRowColor.objects.create(color=col_list[9])  # color object
                d = Date.objects.create(eachrowcolor=erc)  # date object
                ck = CheckAll.objects.create(check='none')
                uck = UnCheckAll.objects.create(uncheck='none')
                c_u = CheckOrUnCheck.objects.create(check_or_uncheck ='block', checkall=ck)
                data = Amount(amount=amnt, date_created=d_created, date=d, year_date=y_d, color=c, eachrowcolor=erc, checkall=ck, uncheckall=uck, checkoruncheck=c_u, author=c_user)
                data.save()
            elif eachMonth == '11':
                erc = EachRowColor.objects.create(color=col_list[10])  # color object
                ck = CheckAll.objects.create(check='none')
                uck = UnCheckAll.objects.create(uncheck='none')
                c_u = CheckOrUnCheck.objects.create(check_or_uncheck ='block', checkall=ck)
                data = Amount(amount=amnt, date_created=d_created, date=d, year_date=y_d, color=c, eachrowcolor=erc, checkall=ck, uncheckall=uck, checkoruncheck=c_u, author=c_user)
                data.save()
            elif eachMonth == '12':
                erc = EachRowColor.objects.create(color=col_list[11])  # color object
                ck = CheckAll.objects.create(check='none')
                d = Date.objects.create(eachrowcolor=erc)  # date object
                uck = UnCheckAll.objects.create(uncheck='none')
                c_u = CheckOrUnCheck.objects.create(check_or_uncheck ='block', checkall=ck)
                data = Amount(amount=amnt, date_created=d_created, date=d, year_date=y_d, color=c, eachrowcolor=erc, checkall=ck, uncheckall=uck, checkoruncheck=c_u, author=c_user)
                data.save()
            
            # col = Color.objects.all()
            # c_col = CommonColor.objects.first()
            # print(col)
            # for obj in col:
            #     obj.color = c_col.color
            #     obj.save()
            return redirect('my-year-home')
    else:
        form = AmountForm()

        
    return render(request, 'myfirstapp/amount_forms.html', {'form': form})


class AmountUpdateView(UserPassesTestMixin, UpdateView):
    model = Amount
    fields = ['amount']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False






# -----------------------------------------
# product_name_in_cart = models.CharField(max_length=100)
# product_price_in_cart = models.DecimalField(max_digits=20, decimal_places=2)
# product_image_in_cart = models.ImageField(upload_to='myshop/images/')
# product_qnty_in_cart = models.IntegerField()
# date_created_in_cart = models.DateField(default=Utils.get_date)