# Generated by Django 4.0.4 on 2023-08-16 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_rename_titlu_resources_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resources',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='resources',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]
