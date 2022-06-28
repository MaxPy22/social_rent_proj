# Generated by Django 4.0.3 on 2022-06-24 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('special_equipment', '0011_equipmentunit_category_equipmentunit_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentunit',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='equipment_units', to=settings.AUTH_USER_MODEL, verbose_name='pacientas'),
        ),
    ]