# Generated by Django 4.2 on 2023-04-08 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('street', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('city', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('state', models.CharField(blank=True, default='', max_length=2, null=True)),
                ('zip_code', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('contact_name', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('contact_phone', models.CharField(blank=True, default='', max_length=50, null=True)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]
