# Generated by Django 4.2 on 2024-07-09 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Номатонро дохил кунед', max_length=50, verbose_name='Ном:')),
                ('last_name', models.CharField(max_length=50, verbose_name='Насаб:')),
                ('midle_name', models.CharField(max_length=50, null=True, verbose_name='Тахаллус:')),
                ('subject', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
    ]