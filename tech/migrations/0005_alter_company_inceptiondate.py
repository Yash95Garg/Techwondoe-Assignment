# Generated by Django 3.2.15 on 2022-09-15 17:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0004_alter_company_inceptiondate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='InceptionDate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
