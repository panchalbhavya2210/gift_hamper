# Generated by Django 4.2.3 on 2024-02-10 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftapp', '0009_usertable_u_address_delete_userdeatiltable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytable',
            name='category_name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='producttable',
            name='p_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
