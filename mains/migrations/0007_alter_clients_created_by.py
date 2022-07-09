# Generated by Django 4.0.6 on 2022-07-08 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mains', '0006_clients_updated_at_alter_clients_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]