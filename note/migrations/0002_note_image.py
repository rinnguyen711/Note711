# Generated by Django 2.1.7 on 2019-02-12 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
