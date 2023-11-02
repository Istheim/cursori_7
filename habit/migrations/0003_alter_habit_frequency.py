# Generated by Django 4.2.6 on 2023-10-31 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0002_alter_habit_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='frequency',
            field=models.CharField(choices=[('Ежедневная', 'Ежедневная'), ('Трехдневная', 'Трехдневная'), ('Еженедельная', 'Еженедельная')], default='Ежедневная', verbose_name='периодичность'),
        ),
    ]