# Generated by Django 4.0.4 on 2023-08-16 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_resources_options_resources_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='created_at',
            field=models.TextField(),
        ),
    ]
