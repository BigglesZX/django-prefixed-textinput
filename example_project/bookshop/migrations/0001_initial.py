# Generated by Django 4.0.5 on 2022-06-14 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('author', models.CharField(max_length=200, verbose_name='Author')),
                ('product_code', models.CharField(max_length=20, verbose_name='Product code')),
                ('pages', models.IntegerField(blank=True, verbose_name='Pages')),
                ('isbn_code', models.CharField(blank=True, max_length=20, verbose_name='ISBN code')),
            ],
        ),
    ]
