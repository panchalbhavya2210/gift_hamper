# Generated by Django 4.2.3 on 2024-01-18 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftapp', '0002_rename_returnproducttablr_returnproducttable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdeatiltable',
            name='u_image',
        ),
        migrations.AddField(
            model_name='usertable',
            name='u_image',
            field=models.ImageField(default='https://cdn-icons-png.flaticon.com/512/6596/6596121.png', upload_to='photos'),
        ),
    ]
