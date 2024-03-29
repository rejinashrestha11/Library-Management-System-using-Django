# Generated by Django 5.0.1 on 2024-02-01 03:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Genre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='Title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bookdetails',
            name='Book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='library_app.book'),
        ),
        migrations.AlterField(
            model_name='bookdetails',
            name='Publisher',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='borrowedbooks',
            name='BookID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_books', to='library_app.book'),
        ),
        migrations.AlterField(
            model_name='borrowedbooks',
            name='BorrowDate',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='borrowedbooks',
            name='UserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_books', to='library_app.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='MembershipDate',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Name',
            field=models.CharField(max_length=100),
        ),
    ]
