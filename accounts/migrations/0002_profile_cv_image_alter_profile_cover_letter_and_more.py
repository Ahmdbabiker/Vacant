# Generated by Django 4.2.11 on 2024-10-28 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cv_image',
            field=models.ImageField(blank=True, null=True, upload_to='cvs'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cover_letter',
            field=models.FileField(blank=True, null=True, upload_to='coverletters'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='cvs'),
        ),
    ]
