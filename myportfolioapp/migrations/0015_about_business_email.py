# Generated by Django 3.1.7 on 2021-09-12 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolioapp', '0014_auto_20210912_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='business_email',
            field=models.EmailField(default='example"gmail.com', max_length=255),
        ),
    ]