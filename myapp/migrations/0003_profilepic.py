# Generated by Django 2.2.7 on 2020-02-26 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_sgup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profilepic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='profilepic/')),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Login')),
            ],
        ),
    ]
