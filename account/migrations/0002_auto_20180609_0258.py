# Generated by Django 2.0.6 on 2018-06-09 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('stock', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=60)),
                ('ratings', models.CharField(max_length=2)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
