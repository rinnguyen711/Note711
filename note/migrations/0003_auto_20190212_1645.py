# Generated by Django 2.1.7 on 2019-02-12 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_note_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='uploaded image'),
        ),
    ]
