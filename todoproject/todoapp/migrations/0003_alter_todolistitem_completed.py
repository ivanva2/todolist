# Generated by Django 5.0.1 on 2024-02-13 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_alter_todolistitem_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolistitem',
            name='completed',
            field=models.BooleanField(),
        ),
    ]