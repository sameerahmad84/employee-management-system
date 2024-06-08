# Generated by Django 5.0.6 on 2024-06-08 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='dapartmentname',
            new_name='deptname',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='fullname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='phonenumber',
            new_name='phone',
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(max_length=50),
        ),
    ]