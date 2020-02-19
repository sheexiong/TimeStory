# Generated by Django 3.0.1 on 2020-02-19 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(default='', max_length=50)),
                ('model', models.CharField(default='', max_length=100)),
                ('availability', models.BooleanField(default=True)),
                ('price', models.IntegerField(default=0)),
                ('status', models.CharField(default='', max_length=20)),
                ('description', models.TextField(default='')),
                ('dial_desp', models.CharField(default='', max_length=100)),
                ('bezel', models.TextField(default='')),
                ('case', models.CharField(default='', max_length=100)),
                ('caseback', models.CharField(default='', max_length=50)),
                ('movement', models.CharField(default='', max_length=100)),
                ('complication', models.TextField(default='')),
                ('strap', models.TextField(default='')),
                ('buckle', models.TextField(default='')),
                ('crystal', models.TextField(default='')),
            ],
        ),
    ]