# Generated by Django 4.0.5 on 2022-08-14 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthanalysis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthanalysis',
            name='path',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
