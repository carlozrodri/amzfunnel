# Generated by Django 4.0.2 on 2022-05-16 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_email_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemsizer',
            name='is_especial',
            field=models.BooleanField(default=False),
        ),
    ]
