# Generated by Django 3.1.5 on 2021-02-11 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_yn', models.BooleanField()),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]
