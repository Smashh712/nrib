# Generated by Django 3.2.7 on 2021-10-14 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0010_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='left',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='right',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
