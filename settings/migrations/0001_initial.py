# Generated by Django 4.2.4 on 2023-09-03 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='forgetpass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='SOME STRING', max_length=40)),
                ('lname', models.CharField(default='SOME STRING', max_length=40)),
                ('email', models.CharField(default='SOME STRING', max_length=100)),
                ('username', models.CharField(default='SOME STRING', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='SOME STRING', max_length=40)),
                ('lname', models.CharField(default='SOME STRING', max_length=40)),
                ('username', models.CharField(default='SOME STRING', max_length=15)),
                ('userpronouns', models.CharField(default='SOME STRING', max_length=20)),
                ('userbio', models.TextField(default='SOME STRING', max_length=250)),
                ('userlink', models.TextField(default='SOME STRING', max_length=400)),
                ('address', models.TextField(default='SOME STRING', max_length=100)),
                ('ph', models.IntegerField()),
                ('email', models.CharField(default='SOME STRING', max_length=100)),
            ],
        ),
    ]
