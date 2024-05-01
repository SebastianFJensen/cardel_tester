# Generated by Django 5.0.1 on 2024-02-22 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_alter_record_by_alter_record_lead_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='Lead',
            field=models.CharField(choices=[('Thomas', 'THOMAS'), ('Vælg', 'Vælg'), ('Magnus', 'MAGNUS'), ('Benjamin', 'BENJAMIN'), ('Stefan', 'Stefan'), ('Jakob', 'JAKOB')], default='Vælg', max_length=10),
        ),
        migrations.AlterField(
            model_name='record',
            name='Status',
            field=models.CharField(choices=[('Lead', 'LEAD'), ('Lost', 'LOST'), ('Negotiation', 'NEGOTIATION'), ('Vælg', 'Vælg'), ('Sendt til DLA', 'SENDT TIL DLA'), ('Lukket aftale', 'LUKKET AFTALE')], default='Vælg', max_length=20),
        ),
    ]