# Generated by Django 3.1.3 on 2021-05-20 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChatAPI', '0003_customresponses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pattern',
            name='user',
        ),
        migrations.DeleteModel(
            name='CustomResponses',
        ),
        migrations.DeleteModel(
            name='Pattern',
        ),
    ]
