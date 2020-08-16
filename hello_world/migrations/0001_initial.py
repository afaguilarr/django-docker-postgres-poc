# Generated by Django 2.2.15 on 2020-08-15 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HelloWorld',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Unknown', max_length=70)),
                ('species', models.CharField(blank=True, default='None', max_length=200)),
                ('galaxy', models.CharField(blank=True, default='Unknown', max_length=200)),
                ('gas', models.BooleanField(default=False)),
                ('population', models.IntegerField()),
                ('birth_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
