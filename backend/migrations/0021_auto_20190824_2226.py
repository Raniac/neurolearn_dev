# Generated by Django 2.1.7 on 2019-08-24 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_data_demo_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_demo',
            name='data_id',
            field=models.CharField(max_length=64),
        ),
    ]
