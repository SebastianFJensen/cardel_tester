# Generated by Django 5.0.1 on 2024-02-22 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0025_alter_record_lead_alter_record_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='By',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='record',
            name='Lead',
            field=models.CharField(choices=[('Magnus', 'MAGNUS'), ('Jakob', 'JAKOB'), ('Benjamin', 'BENJAMIN'), ('Vælg', 'Vælg'), ('Thomas', 'THOMAS'), ('Stefan', 'Stefan')], default='Vælg', max_length=10),
        ),
        migrations.AlterField(
            model_name='record',
            name='Status',
            field=models.CharField(choices=[('Møde booket', 'MØDE BOOKET'), ('Lukket aftale', 'LUKKET AFTALE'), ('Vælg', 'Vælg'), ('Afventer underskrift', 'AFVENTER UNDERSKRIFT'), ('Lost', 'LOST'), ('Bud udarbejdes', 'BUD UDAREJDES'), ('Sendt til DLA', 'SENDT TIL DLA'), ('Negotiation', 'NEGOTIATION'), ('Option udarbejdes', 'OPTION UDAREJDES'), ('Lead', 'LEAD')], default='Vælg', max_length=25),
        ),
    ]
