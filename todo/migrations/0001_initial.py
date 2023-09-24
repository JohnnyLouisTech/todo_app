# Generated by Django 4.2.5 on 2023-09-24 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_created=True)),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('task', models.CharField(max_length=250)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
