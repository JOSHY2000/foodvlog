# Generated by Django 2.2 on 2022-03-10 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20220305_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='available',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]