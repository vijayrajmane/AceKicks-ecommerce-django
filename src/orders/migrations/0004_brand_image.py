# Generated by Django 3.0.7 on 2020-06-20 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
