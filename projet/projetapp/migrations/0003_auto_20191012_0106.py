# Generated by Django 2.2.6 on 2019-10-12 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetapp', '0002_auto_20191012_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='date_add',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='date_update',
            field=models.DateField(null=True),
        ),
    ]