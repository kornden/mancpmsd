# Generated by Django 2.0.5 on 2018-08-14 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cpmsdblog', '0002_auto_20180812_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('education', models.CharField(max_length=500)),
                ('end_year', models.PositiveSmallIntegerField()),
                ('qualification', models.CharField(max_length=20)),
                ('start_experience', models.PositiveSmallIntegerField()),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=13)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=7)),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=7)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='post_title',
            field=models.CharField(max_length=300),
        ),
        migrations.AddField(
            model_name='doctor',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpmsdblog.Unit'),
        ),
    ]
