# Generated by Django 4.2.4 on 2023-11-09 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('savetotravel', '0002_auto_20231109_0336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hoteldestination',
            name='phone_number',
        ),
    ]
