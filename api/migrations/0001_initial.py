# Generated by Django 4.1.6 on 2023-02-08 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('course', models.CharField(choices=[('Python', 'Python'), ('Java', 'Java'), ('C++', 'C++'), ('C#', 'C#'), ('Frontend', 'Frontend')], max_length=40)),
            ],
        ),
    ]
