# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsuserput', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pages',
            old_name='name',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='pages',
            old_name='page',
            new_name='pagina',
        ),
    ]
