# Generated by Django 2.1.7 on 2019-04-17 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20190417_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissions_demo',
            name='task_id',
            field=models.DateTimeField(auto_now=True, verbose_name='Edit the date'),
        ),
    ]