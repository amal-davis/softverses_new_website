# Generated by Django 4.2.4 on 2024-10-29 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softverses_webapp', '0010_whychooseus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(help_text='heading of the portfolio item', max_length=100)),
                ('paragraph', models.TextField(help_text='Paragraph of the portfolio item')),
                ('image', models.ImageField(help_text='Upload an image for the portfolio item', upload_to='portfolio/')),
                ('button_text', models.CharField(blank=True, default='Default Button Text', max_length=255)),
            ],
        ),
    ]
