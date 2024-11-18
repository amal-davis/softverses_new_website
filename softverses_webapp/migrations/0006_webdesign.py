# Generated by Django 4.2.4 on 2024-10-28 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softverses_webapp', '0005_missionvision'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebDesign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Upload the design image', upload_to='web_designs/')),
                ('alt_text', models.CharField(help_text='Alt text for the image', max_length=100)),
            ],
        ),
    ]
