# Generated by Django 2.1.7 on 2019-07-27 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_submissions_demo_enable_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects_Demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(max_length=64, unique=True)),
                ('label', models.CharField(max_length=64, unique=True)),
                ('title', models.CharField(max_length=128)),
                ('introduction', models.TextField(max_length=4096)),
                ('methods', models.TextField(max_length=4096)),
                ('flowchart_url', models.CharField(max_length=128)),
                ('workflow_templates_url', models.CharField(max_length=128)),
                ('data_templates_url', models.CharField(max_length=128)),
            ],
        ),
    ]
