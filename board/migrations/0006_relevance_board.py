# Generated by Django 5.0.2 on 2024-02-27 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_rename_intersr_public_board_interest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relevance_board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=45)),
                ('themes', models.TextField()),
                ('dates', models.DateTimeField()),
            ],
        ),
    ]
