from django.urls import path
from . import views
from .views import AmountUpdateView


urlpatterns = [
    path('home/<int:year>/', views.home, name='my-home'),
    path('', views.year_home, name='my-year-home'),
    path('data_calendar/<int:year>/', views.data_calendar, name='data-calendar'),
    path('save_amount/', views.save_amount, name='save-amount'),
    path('check_one/<int:year>/', views.check_one, name='check-one'),
    path('delete_all/<int:year>/', views.delete_all, name='delete-all'),
    path('check_two/<int:year>/', views.check_two, name='check-two'),
    path('month_details/<int:year>/<int:month>/', views.month_detail, name='month-details'),
    path('delete/<int:pk>/<int:year>/', views.del_item, name='delete-item'),
    path('update/<int:pk>/', AmountUpdateView.as_view(), name='update-item'),

]

