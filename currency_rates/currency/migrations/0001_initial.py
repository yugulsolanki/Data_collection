# Generated by Django 3.0.3 on 2020-06-21 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counrty', models.CharField(max_length=60)),
                ('shortform', models.CharField(max_length=60)),
                ('to_inr', models.CharField(max_length=60)),
            ],
        ),
    ]