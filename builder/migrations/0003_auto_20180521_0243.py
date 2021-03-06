# Generated by Django 2.0.5 on 2018-05-21 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0002_addnews_promoexpansion'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expansion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.Expansion')),
            ],
        ),
        migrations.DeleteModel(
            name='AddNews',
        ),
        migrations.RemoveField(
            model_name='promoexpansion',
            name='expansion',
        ),
        migrations.DeleteModel(
            name='PromoExpansion',
        ),
    ]
