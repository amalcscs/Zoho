# Generated by Django 3.2.20 on 2023-10-07 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0024_alter_expense_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='ends_on',
            field=models.CharField(default='', max_length=50),
        ),
    ]
