# Generated by Django 4.2 on 2024-07-10 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('gender', models.IntegerField(choices=[(1, 'male'), (2, 'Female'), (3, 'other')])),
                ('date_of_birth', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=255)),
                ('photo', models.ImageField(upload_to='static/images')),
            ],
        ),
    ]