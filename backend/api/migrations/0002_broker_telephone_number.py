# Generated by Django 4.0.5 on 2022-07-12 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='broker',
            name='telephone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
