# Generated by Django 3.2.8 on 2021-12-03 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='media')),
                ('document', models.FileField(blank=True, null=True, upload_to='media')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]