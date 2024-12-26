# Generated by Django 5.1.4 on 2024-12-20 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('language', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=10)),
            ],
        ),
    ]