# Generated by Django 4.0.2 on 2022-04-10 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_email_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=100, unique=True),
        ),
    ]
