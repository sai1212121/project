# Generated by Django 5.0.3 on 2024-04-19 04:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_department_studentid_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='studentmarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentmarks', to='app1.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.subject')),
            ],
            options={
                'unique_together': {('student', 'subject')},
            },
        ),
    ]
