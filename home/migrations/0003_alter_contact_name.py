# Generated by Django 4.0.5 on 2022-06-09 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_mobile_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
