# Generated by Django 3.1.1 on 2020-09-27 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20200927_2314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='message',
            new_name='message_text',
        ),
    ]
