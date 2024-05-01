# Generated by Django 5.0.3 on 2024-04-30 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blogpost_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-published_date']},
        ),
        migrations.AddField(
            model_name='blogpost',
            name='status',
            field=models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2),
        ),
    ]