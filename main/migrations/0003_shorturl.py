# Generated by Django 4.2.2 on 2023-08-04 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_contactmessage_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_key', models.CharField(max_length=10, unique=True)),
                ('long_url', models.URLField()),
            ],
        ),
    ]
