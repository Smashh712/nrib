# Generated by Django 3.2.7 on 2021-10-07 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='flag',
            field=models.NullBooleanField(),
        ),
    ]