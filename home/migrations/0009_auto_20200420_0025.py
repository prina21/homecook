# Generated by Django 3.0.2 on 2020-04-19 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_vinfo_kitchen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinfo',
            name='Username',
            field=models.CharField(max_length=100),
        ),
    ]