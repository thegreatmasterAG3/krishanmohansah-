# Generated by Django 4.2 on 2023-04-21 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krishan', '0003_rename_contact_contactform_delete_imagepost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ContactForm',
        ),
    ]