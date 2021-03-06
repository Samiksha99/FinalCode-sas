# Generated by Django 3.0.4 on 2020-03-31 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_pulses'),
    ]

    operations = [
        migrations.CreateModel(
            name='oils',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('price', models.CharField(max_length=100)),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='vegs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('price', models.CharField(max_length=100)),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
