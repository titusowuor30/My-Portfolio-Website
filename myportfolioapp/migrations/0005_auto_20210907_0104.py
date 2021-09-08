# Generated by Django 3.1.7 on 2021-09-06 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolioapp', '0004_auto_20210907_0100'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('phone', models.CharField(default='+254743793901', max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='teams',
            new_name='team',
        ),
        migrations.DeleteModel(
            name='About',
        ),
    ]
