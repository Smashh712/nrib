# Generated by Django 3.2.7 on 2021-10-09 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0002_question_flag'),
    ]

    operations = [
        migrations.CreateModel(
            name='issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('moderator', models.TextField()),
                ('agree', models.TextField()),
                ('disagree', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='issue_reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('like', models.PositiveIntegerField()),
                ('side', models.NullBooleanField()),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.issue')),
            ],
        ),
        migrations.RenameField(
            model_name='question',
            old_name='flag',
            new_name='side',
        ),
        migrations.CreateModel(
            name='issue_rereply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('like', models.PositiveIntegerField()),
                ('issue_reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.issue_reply')),
            ],
        ),
    ]