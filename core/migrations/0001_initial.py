# Generated by Django 3.2.12 on 2022-02-22 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created', null=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified', null=True, verbose_name='Modified at')),
                ('is_active', models.BooleanField(db_column='cs_active', default=True, verbose_name='Active')),
                ('name', models.CharField(db_column='tx_name', max_length=128, verbose_name='Name')),
                ('phone', models.CharField(db_column='tx_phone', max_length=32, verbose_name='Phone')),
                ('category', models.CharField(choices=[('0', 'Family'), ('1', 'Friend'), ('2', 'Other')], db_column='cs_category', default='0', max_length=2, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'db_table': 'contact',
                'managed': True,
            },
        ),
    ]
