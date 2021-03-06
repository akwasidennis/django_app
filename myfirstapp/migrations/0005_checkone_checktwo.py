# Generated by Django 3.0.8 on 2019-08-02 06:32

from django.db import migrations, models
import django.db.models.deletion
import myfirstapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0004_checkoruncheck_checkall'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_one', models.CharField(default='none', max_length=20)),
                ('dates', models.DateField(default=myfirstapp.models.CheckOne.date_now)),
            ],
        ),
        migrations.CreateModel(
            name='CheckTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_two', models.CharField(default='none', max_length=20)),
                ('dates', models.DateField(default=myfirstapp.models.CheckTwo.date_now)),
                ('checkone', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myfirstapp.CheckOne')),
            ],
        ),
    ]
