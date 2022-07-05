# Generated by Django 4.0.5 on 2022-07-04 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='media')),
                ('text', models.TextField(blank=True)),
                ('rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='media')),
                ('rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('email', models.EmailField(max_length=400)),
                ('Review', models.TextField(blank=True)),
                ('slug', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('price', models.IntegerField()),
                ('discount_price', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='media')),
                ('description', models.TextField(blank=True)),
                ('specification', models.TextField(blank=True)),
                ('slug', models.TextField(unique=True)),
                ('labels', models.CharField(choices=[('new', 'New'), ('hot', 'Hot'), ('sale', 'Sale'), ('', 'default')], max_length=100)),
                ('stock', models.CharField(choices=[('In Stock', 'In Stock'), ('Out Stock', 'Out Stock')], max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.subcategory')),
            ],
        ),
    ]
