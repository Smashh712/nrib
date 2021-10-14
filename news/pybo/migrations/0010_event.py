# Generated by Django 3.2.7 on 2021-10-13 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0009_auto_20211014_0150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('side', models.NullBooleanField()),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pybo.topic')),
            ],
        ),
    ]