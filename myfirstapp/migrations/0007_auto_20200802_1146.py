# Generated by Django 3.0.8 on 2020-08-02 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0006_auto_20200802_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checktwo',
            name='checkone',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myfirstapp.CheckOne'),
        ),
    ]
