# Generated by Django 3.2.11 on 2022-06-12 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_broker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broker',
            name='houses',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.house'),
        ),
    ]