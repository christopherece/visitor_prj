# Generated by Django 4.2.5 on 2023-09-21 08:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0006_alter_visitor_is_signout'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='signout_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
