# Generated by Django 2.2.26 on 2022-03-15 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crowdbotic_lite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionPlans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tier', models.TextField(blank=True, max_length=50)),
                ('price', models.IntegerField(blank=True)),
                ('date_created', models.DateTimeField(blank=True)),
                ('date_updated', models.DateTimeField(blank=True)),
                ('crowdbotic_lite', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscriptionplans_crowdbotic_lite', to='crowdbotic_lite.GenerateModels')),
            ],
        ),
    ]
