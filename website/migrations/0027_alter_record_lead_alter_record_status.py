# Generated by Django 5.0.1 on 2024-02-22 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_alter_record_by_alter_record_lead_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='Lead',
            field=models.CharField(choices=[('Magnus', 'MAGNUS'), ('Stefan', 'Stefan'), ('Vælg', 'Vælg'), ('Jakob', 'JAKOB'), ('Thomas', 'THOMAS'), ('Benjamin', 'BENJAMIN')], default='Vælg', max_length=10),
        ),
        migrations.AlterField(
            model_name='record',
            name='Status',
            field=models.CharField(choices=[('Vælg', 'Vælg'), ('Lead', 'LEAD'), ('Lost', 'LOST'), ('Bud udarbejdes', 'BUD UDAREJDES'), ('Sendt til DLA', 'SENDT TIL DLA'), ('Afventer underskrift', 'AFVENTER UNDERSKRIFT'), ('Option udarbejdes', 'OPTION UDAREJDES'), ('Møde booket', 'MØDE BOOKET'), ('Negotiation', 'NEGOTIATION'), ('Lukket aftale', 'LUKKET AFTALE')], default='Vælg', max_length=25),
        ),
    ]
