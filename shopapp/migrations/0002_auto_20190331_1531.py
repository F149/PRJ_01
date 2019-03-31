# Generated by Django 2.1.7 on 2019-03-31 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('short_description', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='book_images/')),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='bookshop',
            name='logo',
            field=models.ImageField(upload_to='bookshop_logo/'),
        ),
        migrations.AlterField(
            model_name='bookshop',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bookshop', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='bookshop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopapp.BookShop'),
        ),
    ]
