# Generated by Django 5.0.2 on 2024-02-27 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_remove_authors_public_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='public_board',
            name='intersr',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]