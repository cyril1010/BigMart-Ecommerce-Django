# Generated by Django 5.1.3 on 2024-11-14 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_rename_feedbackdb_contactdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdb',
            name='contact',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
