# Generated by Django 3.0.8 on 2020-08-02 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0005_checkone_checktwo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checktwo',
            name='checkone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfirstapp.CheckOne'),
        ),
    ]