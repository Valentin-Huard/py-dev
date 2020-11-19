# Generated by Django 3.1.3 on 2020-11-19 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0004_datas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isApproved', models.BooleanField(default=False)),
                ('ligne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.ligne')),
            ],
        ),
    ]