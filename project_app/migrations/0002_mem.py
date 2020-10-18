# Generated by Django 3.1.2 on 2020-10-09 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('tags', models.CharField(max_length=256)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='picture')),
                ('comments', models.ManyToManyField(to='project_app.Comment')),
            ],
        ),
    ]