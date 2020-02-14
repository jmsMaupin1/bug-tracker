# Generated by Django 3.0.3 on 2020-02-14 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug_tracker', '0006_auto_20200214_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_status',
            field=models.CharField(choices=[('NEW', 'New'), ('INPROG', 'In Progress')], default='NEW', max_length=11),
        ),
    ]
