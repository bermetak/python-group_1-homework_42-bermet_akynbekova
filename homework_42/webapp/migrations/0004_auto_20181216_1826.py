# Generated by Django 2.1.4 on 2018-12-16 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20181216_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorit',
            name='article',
        ),
        migrations.RemoveField(
            model_name='favorit',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='favorit',
            field=models.ManyToManyField(to='webapp.Article'),
        ),
        migrations.DeleteModel(
            name='Favorit',
        ),
    ]
