# Generated by Django 5.0.1 on 2024-02-01 03:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_alter_book_genre_alter_book_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Genre',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='Title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='bookdetails',
            name='Book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='library_app.book'),
        ),
        migrations.AlterField(
            model_name='bookdetails',
            name='Publisher',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='borrowedbooks',
            name='BookID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.book'),
        ),
        migrations.AlterField(
            model_name='borrowedbooks',
            name='BorrowDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='borrowedbooks',
            name='UserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='MembershipDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='Name',
            field=models.CharField(max_length=255),
        ),
    ]
