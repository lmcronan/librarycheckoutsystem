# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libcheckoutsys', '0004_book_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[(b'On Shelf', b'On Shelf'), (b'Borrowed', b'Borrowed'), (b'Overdue', b'Overdue'), (b'Lost', b'Lost')], default=b'On Shelf', max_length=10),
        ),
    ]
