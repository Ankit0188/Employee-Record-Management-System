# Generated by Django 3.1.1 on 2023-07-17 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetail',
            name='empcode',
            field=models.CharField(max_length=100, null=True),
        ),
    ]