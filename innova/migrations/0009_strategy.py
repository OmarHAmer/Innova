# Generated by Django 4.2.4 on 2023-10-08 19:26

from django.db import migrations, models
import innova.models


class Migration(migrations.Migration):

    dependencies = [
        ('innova', '0008_company_information_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField()),
                ('Last_update_date', models.DateTimeField(auto_now=True)),
                ('Last_update_by', models.IntegerField()),
                ('subject', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('Image', models.ImageField(upload_to=innova.models.upload_image)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
