# Generated by Django 2.2.3 on 2019-07-27 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halfapp', '0003_remove_account_youwork'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='youwork',
            field=models.CharField(choices=[('New', '신규'), ('Work', '출근'), ('NotWork', '결근')], default='New', max_length=20),
        ),
    ]