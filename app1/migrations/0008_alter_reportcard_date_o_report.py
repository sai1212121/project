# Generated by Django 5.0.3 on 2024-04-19 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_reportcard_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportcard',
            name='date_o_report',
            field=models.DateField(auto_now_add=True),
        ),
    ]
