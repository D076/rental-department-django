# Generated by Django 3.1.5 on 2021-01-20 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('apartment_rooms', models.IntegerField()),
                ('apartment_price', models.IntegerField()),
                ('apartment_status', models.CharField(max_length=50)),
                ('id_apartment', models.AutoField(db_column='id_apartment', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'apartment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BronList',
            fields=[
                ('bron_number', models.CharField(blank=True, max_length=20, null=True)),
                ('id_bron_list', models.AutoField(db_column='id_bron_list', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'bron_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CleanRequest',
            fields=[
                ('clean_request_data', models.DateField()),
                ('id_clean_request', models.AutoField(db_column='id_clean_request', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'clean_request',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_name', models.CharField(max_length=100)),
                ('customer_phone', models.CharField(max_length=20)),
                ('customer_pasport', models.CharField(max_length=20)),
                ('id_customer', models.AutoField(db_column='id_customer', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ResidDoc',
            fields=[
                ('doc_date_start', models.DateField()),
                ('doc_date_end', models.DateField(blank=True, null=True)),
                ('doc_price', models.IntegerField(blank=True, null=True)),
                ('id_doc', models.AutoField(db_column='id_doc', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'redis_doc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AdminWorker',
            fields=[
                ('admin_worker_name', models.CharField(max_length=100)),
                ('id_admin_worker', models.AutoField(db_column='id_admin_worker', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'admin_worker',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CleanWorker',
            fields=[
                ('clean_worker_name', models.CharField(max_length=100)),
                ('id_clean_worker', models.AutoField(db_column='id_clean_worker', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'clean_worker',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserExtent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_extent', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
