# Generated by Django 2.0.4 on 2018-04-10 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20180404_1928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventindexpage',
            name='excerpt_en',
        ),
        migrations.RemoveField(
            model_name='eventindexpage',
            name='excerpt_fr',
        ),
        migrations.RemoveField(
            model_name='eventindexpage',
            name='excerpt_sp',
        ),
        migrations.RemoveField(
            model_name='eventindexpage',
            name='heading_en',
        ),
        migrations.RemoveField(
            model_name='eventindexpage',
            name='heading_fr',
        ),
        migrations.RemoveField(
            model_name='eventindexpage',
            name='heading_sp',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='additional_information_en',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='additional_information_fr',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='additional_information_sp',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='date_end',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='date_start',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='description_fr',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='description_sp',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='event_type',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='heading_en',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='heading_fr',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='heading_sp',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='location',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='registration_link',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='subheading_en',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='subheading_fr',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='subheading_sp',
        ),
        migrations.DeleteModel(
            name='EventType',
        ),
    ]