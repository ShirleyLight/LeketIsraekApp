# Generated by Django 3.2.18 on 2023-06-13 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeketIsraelApp', '0011_alter_leket_db_new_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leket_db_new',
            name='group',
            field=models.CharField(max_length=100, null=True, verbose_name='group'),
        ),
    ]
