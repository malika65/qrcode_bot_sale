# Generated by Django 3.2.8 on 2021-11-09 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon_generate', '0006_alter_subscriber_sub_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='sub_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]