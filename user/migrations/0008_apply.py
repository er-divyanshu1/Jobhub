# Generated by Django 4.2.3 on 2023-08-22 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_selectedstudent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='')),
                ('applydate', models.DateField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.job')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.studentuser')),
            ],
        ),
    ]
