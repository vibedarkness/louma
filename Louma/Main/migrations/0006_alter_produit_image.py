# Generated by Django 3.2.3 on 2022-05-16 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_auto_20220515_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
