# Generated by Django 4.0.3 on 2022-06-29 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('special_equipment', '0021_equipmentmodel_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentunit',
            name='returning_date',
            field=models.DateField(blank=True, db_index=True, null=True, verbose_name='numatomas grąžinimas: '),
        ),
    ]
