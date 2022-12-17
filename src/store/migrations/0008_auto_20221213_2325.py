# Generated by Django 3.1.7 on 2022-12-13 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20221213_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='color',
            field=models.ManyToManyField(blank=True, null=True, to='store.Color'),
        ),
        migrations.AlterField(
            model_name='products',
            name='size',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], default='S', max_length=2, null=True),
        ),
    ]
