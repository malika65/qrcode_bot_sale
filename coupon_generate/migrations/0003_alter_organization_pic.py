# Generated by Django 3.2.8 on 2021-11-02 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon_generate', '0002_auto_20211102_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/organization'),
        ),
    ]