# Generated by Django 3.2.3 on 2022-05-15 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='ecommerce/ping')),
                ('prix', models.IntegerField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('id_vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.vendeur')),
            ],
        ),
    ]
