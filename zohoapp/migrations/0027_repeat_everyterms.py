# Generated by Django 3.2.20 on 2023-10-07 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0026_alter_expense_ends_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='repeat_everyterms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Terms', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
