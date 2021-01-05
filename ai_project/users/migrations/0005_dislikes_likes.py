# Generated by Django 3.1.1 on 2020-12-31 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_water'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dislikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.TextField(max_length=10, null=True)),
                ('food_names', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.TextField(max_length=10, null=True)),
                ('food_names', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
