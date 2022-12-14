# Generated by Django 4.0 on 2022-08-24 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PolicyModel',
            fields=[
                ('policy_key', models.AutoField(primary_key=True, serialize=False)),
                ('quote_id', models.IntegerField()),
                ('policy_term', models.CharField(max_length=20)),
                ('policy_effective_date', models.DateField()),
                ('policy_end_date', models.DateField()),
                ('status', models.CharField(default='None', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='QuoteModel',
            fields=[
                ('quote_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('hno', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('residance_type', models.CharField(max_length=50)),
                ('residance_use', models.CharField(max_length=100)),
                ('detached_structure', models.CharField(max_length=100)),
                ('market_value', models.DecimalField(decimal_places=2, max_digits=100)),
                ('year_build', models.IntegerField()),
                ('square_foot_value', models.IntegerField()),
                ('dwelling_style', models.CharField(max_length=50)),
                ('roof_material', models.CharField(max_length=50)),
                ('garage_type', models.CharField(max_length=50)),
                ('numfullBaths', models.IntegerField()),
                ('numhalfBaths', models.IntegerField()),
                ('has_swimming_pool', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
            ],
        ),
    ]
