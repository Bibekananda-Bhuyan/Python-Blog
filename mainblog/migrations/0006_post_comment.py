# Generated by Django 3.0.5 on 2020-04-20 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainblog', '0005_contactquery_extrapages_websiteuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300)),
                ('useremail', models.CharField(max_length=500)),
                ('comment', models.TextField(max_length=5000)),
                ('added_date', models.DateField(auto_now=True)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainblog.Post')),
            ],
        ),
    ]
