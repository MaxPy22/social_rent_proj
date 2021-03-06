# Generated by Django 4.0.3 on 2022-06-18 13:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(help_text='nurodyti kateogoriją (pvz. judėjimo, higienos reikmenys ir t.t.)', max_length=156, verbose_name='Spec. priemonių kategorijos')),
            ],
            options={
                'verbose_name': 'Spec. priemonės kategorija',
                'verbose_name_plural': 'spec. priemonių kategorijos',
                'ordering': ['category_title'],
            },
        ),
        migrations.CreateModel(
            name='EquipmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=156, verbose_name='gaminio modelio pavadinimas')),
                ('category', models.ManyToManyField(help_text='nurodykit priemonės kategoriją', related_name='equipment_models', to='special_equipment.category', verbose_name='Kategorija')),
            ],
            options={
                'verbose_name': 'spec. priemonės modelis',
                'verbose_name_plural': 'spec. priemonių modeliai',
                'ordering': ['model_name'],
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_title', models.CharField(help_text='nurodyti konkrečią rūšį (pvz. neigaliojo vežimėlis, funkcinė lova ir pan.)', max_length=156, verbose_name='rūšis')),
            ],
            options={
                'verbose_name': 'spec.priemonės rūšis',
                'verbose_name_plural': 'spec.priemonių rūšys',
                'ordering': ['type_title'],
            },
        ),
        migrations.CreateModel(
            name='EquipmentUnit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='apskaitomo priemonės vieneto unikalus ID', primary_key=True, serialize=False, verbose_name='id')),
                ('status', models.CharField(blank=True, choices=[('k', 'sandėlyje/prieinama'), ('p', 'paimta'), ('r', 'remonuotina'), ('n', 'naudojimui netinkama(nurašytina)')], db_index=True, default='ok', max_length=1, verbose_name='prieinamumas')),
                ('equipment_model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='equipment_models', to='special_equipment.equipmentmodel', verbose_name='spec. priemonė')),
            ],
            options={
                'verbose_name': 'spec. priemonės vienetas',
                'verbose_name_plural': 'spec. priemonių atsargos',
            },
        ),
        migrations.AddField(
            model_name='equipmentmodel',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='equipment_models', to='special_equipment.type', verbose_name='priemonės rūšis'),
        ),
    ]
