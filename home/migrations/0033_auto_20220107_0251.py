# Generated by Django 3.2.4 on 2022-01-07 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_auto_20220107_0042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupmeuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='groupmeuser',
            name='user',
        ),
        migrations.DeleteModel(
            name='GroupmeGroup',
        ),
        migrations.DeleteModel(
            name='GroupmeUser',
        ),
    ]
