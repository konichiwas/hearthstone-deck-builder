# Generated by Django 2.0.5 on 2018-05-23 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0004_promo_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='promo',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='promo',
            name='order',
            field=models.PositiveIntegerField(default=1),
        ),
    ]