# Generated by Django 2.1.5 on 2019-01-25 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IceCream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavor', models.CharField(max_length=50)),
                ('base', models.CharField(max_length=50)),
                ('available', models.CharField(max_length=50)),
                ('featured', models.BooleanField(null=True)),
                ('date_churned', models.DateField(null=True)),
            ],
        ),
    ]