# Generated by Django 4.2.14 on 2024-10-23 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_cvorders_address_alter_cvorders_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvorders',
            name='langugaes',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
