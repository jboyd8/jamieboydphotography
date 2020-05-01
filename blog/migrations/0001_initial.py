# Generated by Django 3.0.5 on 2020-05-01 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=200)),
                ('blog_body', models.TextField(blank=True)),
                ('genre', models.CharField(choices=[('landscapes', 'Landscapes'), ('landscapes', 'Portraits'), ('cityscapes', 'Cityscapes'), ('technical', 'Technical'), ('general', 'General')], max_length=30)),
                ('date_added', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
    ]
