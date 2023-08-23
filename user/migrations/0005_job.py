# Generated by Django 4.2.3 on 2023-08-19 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_delete_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_date', models.DateField()),
                ('e_date', models.DateField()),
                ('job_title', models.CharField(max_length=100)),
                ('salary', models.FloatField(max_length=50)),
                ('img', models.FileField(upload_to='')),
                ('discription', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=100)),
                ('education', models.CharField(max_length=100)),
                ('skill', models.CharField(max_length=200)),
                ('experince', models.CharField(max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.recruiter')),
            ],
        ),
    ]
