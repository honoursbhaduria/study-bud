# Generated by Django 5.1.6 on 2025-02-22 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_participents_room_participants'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
