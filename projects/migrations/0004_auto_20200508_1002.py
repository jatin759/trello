# Generated by Django 2.2.4 on 2020-05-08 04:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0003_auto_20200508_0959'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProject',
            new_name='UserProjectRelation',
        ),
    ]
