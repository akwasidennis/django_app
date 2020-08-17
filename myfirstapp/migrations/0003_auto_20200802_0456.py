# Generated by Django 3.0.8 on 2020-08-02 04:56

from django.db import migrations, models
import myfirstapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0002_auto_20200801_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkall',
            name='dates',
            field=models.DateField(default=myfirstapp.models.CheckAll.date_now),
        ),
        migrations.AddField(
            model_name='checkoruncheck',
            name='dates',
            field=models.DateField(default=myfirstapp.models.CheckOrUnCheck.date_now),
        ),
        migrations.AddField(
            model_name='color',
            name='dates',
            field=models.DateField(default=myfirstapp.models.Color.date_now),
        ),
        migrations.AddField(
            model_name='commoncolor',
            name='dates',
            field=models.DateField(default=myfirstapp.models.CommonColor.date_now),
        ),
        migrations.AddField(
            model_name='eachrowcolor',
            name='dates',
            field=models.DateField(default=myfirstapp.models.EachRowColor.date_now),
        ),
        migrations.AddField(
            model_name='uncheckall',
            name='dates',
            field=models.DateField(default=myfirstapp.models.UnCheckAll.date_now),
        ),
    ]
