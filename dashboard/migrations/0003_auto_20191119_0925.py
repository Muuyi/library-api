# Generated by Django 2.2.7 on 2019-11-19 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20191119_0804'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title']},
        ),
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
    ]
