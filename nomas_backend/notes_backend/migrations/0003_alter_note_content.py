# Generated by Django 4.1.7 on 2023-02-23 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_backend', '0002_alter_note_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(max_length=200, null='Null'),
        ),
    ]