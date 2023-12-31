# Generated by Django 4.2.5 on 2023-11-28 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('savetotravel', '0008_booked_events_payment_booked_events_event_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('deposit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='savetotravel.payments')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='savetotravel.events')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='savetotravel.user')),
            ],
        ),
    ]
