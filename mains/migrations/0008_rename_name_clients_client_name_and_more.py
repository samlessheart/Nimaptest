# Generated by Django 4.0.6 on 2022-07-10 05:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mains', '0007_alter_clients_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clients',
            old_name='name',
            new_name='client_name',
        ),
        migrations.AlterField(
            model_name='clients',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projects',
            name='assign_to',
            field=models.ManyToManyField(blank=True, related_name='projects', to=settings.AUTH_USER_MODEL),
        ),
    ]
