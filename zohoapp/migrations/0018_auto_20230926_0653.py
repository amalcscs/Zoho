# Generated by Django 3.2.20 on 2023-09-26 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0017_auto_20230926_0547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliverychellan',
            old_name='customer',
            new_name='cu',
        ),
        migrations.AddField(
            model_name='customer',
            name='cr_dr',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchase_order',
            name='custo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.customer'),
        ),
        migrations.AddField(
            model_name='purchasebills',
            name='cusname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.customer'),
        ),
        migrations.AddField(
            model_name='recur_itemtable',
            name='hsncode',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recurring_bills',
            name='cname_recur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.customer'),
        ),
        migrations.AddField(
            model_name='recurring_invoice',
            name='attachment',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='recurring_invoice',
            name='balance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recurring_invoice',
            name='comments',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='recurring_invoice',
            name='gstnum',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='recurring_invoice',
            name='gsttr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='recurring_invoice',
            name='paid',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recurring_invoice',
            name='payment_method',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='recurring_invoice',
            name='reinvoiceno',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='recurring_invoice',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='recurring_invoice',
            name='cadrs',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='recurring_invoice',
            name='cemail',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='recurring_invoice',
            name='cname',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
