# Generated by Django 3.2.9 on 2022-02-22 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practo_demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor_details',
            options={'verbose_name_plural': 'Doctor Details'},
        ),
        migrations.AlterModelOptions(
            name='user_data',
            options={'verbose_name_plural': 'User Data'},
        ),
    ]
