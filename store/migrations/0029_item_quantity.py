# Generated by Django 4.1.7 on 2023-04-26 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_alter_order_mobilenumber_alter_profile_mobilenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]