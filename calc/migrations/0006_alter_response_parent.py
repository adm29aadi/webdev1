# Generated by Django 3.2 on 2021-06-12 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0005_alter_response_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calc.response'),
        ),
    ]
