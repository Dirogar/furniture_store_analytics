# Generated by Django 5.0.6 on 2024-08-02 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_remove_profile_store'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AddField(
            model_name='profile',
            name='uuid',
            field=models.UUIDField(default=1231, primary_key=True, serialize=False, verbose_name='uuid'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='work_position',
            field=models.TextField(blank=True, max_length=20, verbose_name='Должность'),
        ),
    ]
