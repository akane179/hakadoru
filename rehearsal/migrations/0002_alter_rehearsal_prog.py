# Generated by Django 3.2.7 on 2021-09-09 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rehearsal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rehearsal',
            name='prog',
            field=models.CharField(choices=[(' ', ' '), ('Started', 'Started'), ('DONE!!!', 'DONE!!!')], default='0', max_length=10),
        ),
    ]
