# Generated by Django 2.1.4 on 2018-12-16 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20181216_1738'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorit',
            options={'verbose_name': 'Избранное', 'verbose_name_plural': 'Избранные'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='webapp.Comment'),
        ),
    ]
