# Generated by Django 3.1 on 2020-08-23 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0003_auto_20200823_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gaiasource',
            name='id',
        ),
        migrations.AlterField(
            model_name='gaiasource',
            name='source_id',
            field=models.PositiveBigIntegerField(help_text='1000225938242805248', primary_key=True, serialize=False),
        ),
    ]
