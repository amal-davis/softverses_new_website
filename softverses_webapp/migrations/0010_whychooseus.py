# Generated by Django 4.2.4 on 2024-10-29 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softverses_webapp', '0009_about_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhyChooseUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the main title', max_length=200)),
                ('sub_title', models.CharField(help_text='Enter the subtitle', max_length=200)),
                ('left_heading', models.CharField(help_text='Heading for the left text block', max_length=200)),
                ('left_description', models.TextField(help_text='Description for the left text block')),
                ('right_heading', models.CharField(help_text='Heading for the right text block', max_length=200)),
                ('right_description', models.TextField(help_text='Description for the right text block')),
            ],
        ),
    ]
