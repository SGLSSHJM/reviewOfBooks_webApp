# Generated by Django 4.0.4 on 2022-05-02 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_remove_book_pub_date_book_desc_book_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='remark',
            name='user',
            field=models.CharField(default='匿名', max_length=64),
        ),
    ]
