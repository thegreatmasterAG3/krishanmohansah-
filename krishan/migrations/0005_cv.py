# Generated by Django 4.2 on 2023-04-22 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krishan', '0004_contact_delete_contactform'),
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_file', models.FileField(upload_to='pdfs/')),
            ],
        ),
    ]
