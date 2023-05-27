# Generated by Django 4.2.1 on 2023-05-07 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SupervisorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=1000)),
            ],
            options={
                'verbose_name': 'Profile de Supervisor',
                'verbose_name_plural': 'Profiles de Supervisors',
            },
        ),
    ]