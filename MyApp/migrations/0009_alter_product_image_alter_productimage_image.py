# Generated by Django 5.1.6 on 2025-04-14 23:58

import storages.backends.s3
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0008_merge_20250331_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=storages.backends.s3.S3Storage(), upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(storage=storages.backends.s3.S3Storage(), upload_to='products/additional_images/'),
        ),
    ]
