# Generated by Django 2.1.7 on 2019-05-13 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_data_demo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissions_demo',
            name='task_id',
            field=models.CharField(max_length=64),
        ),
    ]
