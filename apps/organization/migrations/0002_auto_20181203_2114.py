# Generated by Django 2.1.3 on 2018-12-03 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='image',
            field=models.ImageField(null=True, upload_to='org/%Y/%m', verbose_name='Logo'),
        ),
    ]