# Generated by Django 4.0.7 on 2024-08-15 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='posts_count',
            new_name='ride_count',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='subscriber_count',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='subscription_count',
        ),
    ]
