# Generated by Django 5.0.1 on 2024-03-05 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0034_record_moedestatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='Opfølgningsdato',
            field=models.DateField(blank=True, null=True),
        ),
    ]
