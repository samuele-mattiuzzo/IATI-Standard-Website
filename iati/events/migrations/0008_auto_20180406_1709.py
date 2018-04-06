# Generated by Django 2.0.4 on 2018-04-06 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20180405_1814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventindexpage',
            old_name='excerpt_en',
            new_name='excerpt',
        ),
        migrations.RenameField(
            model_name='eventindexpage',
            old_name='heading_en',
            new_name='heading',
        ),
        migrations.RenameField(
            model_name='eventpage',
            old_name='additional_information_en',
            new_name='additional_information',
        ),
        migrations.RenameField(
            model_name='eventpage',
            old_name='additional_information_es',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='eventpage',
            old_name='heading_en',
            new_name='heading',
        ),
        migrations.RenameField(
            model_name='eventpage',
            old_name='heading_es',
            new_name='subheading',
        ),
        migrations.RenameField(
            model_name='eventtype',
            old_name='name_en',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='eventindexpage',
            name='excerpt_es',
        ),
        migrations.RemoveField(
            model_name='eventindexpage',
            name='excerpt_fr',
        ),
        migrations.RemoveField(
            model_name='eventindexpage',
            name='heading_es',
        ),
        migrations.RemoveField(
            model_name='eventindexpage',
            name='heading_fr',
        ),
        migrations.RemoveField(
            model_name='eventindexpage',
            name='title_es',
        ),
        migrations.RemoveField(
            model_name='eventindexpage',
            name='title_fr',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='additional_information_fr',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='description_es',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='description_fr',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='heading_fr',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='subheading_en',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='subheading_es',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='subheading_fr',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='title_es',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='title_fr',
        ),
        migrations.RemoveField(
            model_name='eventtype',
            name='name_es',
        ),
        migrations.RemoveField(
            model_name='eventtype',
            name='name_fr',
        ),
    ]
