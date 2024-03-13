# Generated by Django 5.0.3 on 2024-03-11 17:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=64)),
                ('bourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registeredStocks', to='stockmanager.bourse')),
            ],
        ),
    ]