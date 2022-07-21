# Generated by Django 4.0.5 on 2022-07-14 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_ad_brand_review_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.brand'),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.CharField(max_length=400),
        ),
    ]
