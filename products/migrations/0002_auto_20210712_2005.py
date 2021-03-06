# Generated by Django 3.0.1 on 2021-07-12 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='dimensions',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(blank=True, default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(blank=True, default='dimensions', max_length=1024),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, default='example', max_length=254),
            preserve_default=False,
        ),
    ]
