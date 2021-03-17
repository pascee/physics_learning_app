# Generated by Django 3.1.5 on 2021-03-01 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drag_Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj_name', models.CharField(max_length=200)),
                ('drag_coeficient', models.DecimalField(decimal_places=3, max_digits=10)),
                ('current_speed', models.DecimalField(decimal_places=3, max_digits=13)),
                ('gravitational_constant', models.DecimalField(decimal_places=2, max_digits=5)),
                ('obj_mass', models.DecimalField(decimal_places=3, max_digits=15)),
            ],
        ),
    ]
