# Generated by Django 3.0a1 on 2019-10-06 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.CharField(choices=[('TC', 'Tecnologia'), ('CR', 'Curiosidades'), ('GR', 'Geral')], default='GR', max_length=2),
        ),
    ]