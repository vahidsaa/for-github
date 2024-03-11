# Generated by Django 4.2.4 on 2024-03-08 06:17

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
            name='ShippingAdress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(max_length=555)),
                ('codeposti', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(blank=True, max_length=55, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'ادرس های تحویل',
            },
        ),
    ]
