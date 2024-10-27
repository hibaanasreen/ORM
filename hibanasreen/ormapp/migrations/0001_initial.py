# Generated by Django 5.1.2 on 2024-10-22 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bankloan',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('ifsc', models.CharField(max_length=30)),
                ('mobno', models.IntegerField()),
                ('accno', models.IntegerField(max_length=20, primary_key='accno', serialize=False)),
                ('loanamount', models.IntegerField()),
            ],
        ),
    ]
