# Generated by Django 3.1.1 on 2023-06-21 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empcode', models.CharField(max_length=50)),
                ('empdept', models.CharField(max_length=100, null=True)),
                ('empdesignation', models.CharField(max_length=100, null=True)),
                ('empcontact', models.CharField(max_length=15, null=True)),
                ('empgender', models.CharField(max_length=50, null=True)),
                ('empjoiningdate', models.DateField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
