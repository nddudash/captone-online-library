# Generated by Django 3.2.7 on 2021-10-08 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_text'),
        ('custom_user', '0003_merge_20211007_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='checked_out_books',
            field=models.ManyToManyField(blank=True, to='book.Book'),
        ),
    ]
