# Generated by Django 3.0.3 on 2020-02-14 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug_tracker', '0003_auto_20200214_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_status',
            field=models.CharField(choices=[('FRS', 'New'), ('INPROG', 'Sophomore'), ('JRD', 'Junior'), ('SR', 'Senior')], default='FRS', max_length=11),
        ),
    ]