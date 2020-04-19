# Generated by Django 2.2 on 2020-03-30 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Online_Hobbies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('online_hobby_name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('get_started', models.CharField(max_length=100)),
            ],
        ),
    ]
