# Generated by Django 3.2.15 on 2022-09-15 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0005_alter_company_inceptiondate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='InceptionDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
