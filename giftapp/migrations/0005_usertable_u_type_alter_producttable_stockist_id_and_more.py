# Generated by Django 4.2.3 on 2024-02-04 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('giftapp', '0004_alter_usertable_u_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertable',
            name='u_type',
            field=models.CharField(choices=[(0, 'User'), (1, 'Seller')], default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='producttable',
            name='stockist_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giftapp.usertable'),
        ),
        migrations.AlterField(
            model_name='usertable',
            name='u_image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.DeleteModel(
            name='giftstockisttable',
        ),
    ]
