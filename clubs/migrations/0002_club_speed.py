# Generated by Django 3.2 on 2022-01-07 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='speed',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
