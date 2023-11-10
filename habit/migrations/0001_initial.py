# Generated by Django 4.2.6 on 2023-10-28 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=25, verbose_name='место')),
                ('timing', models.TimeField(verbose_name='время')),
                ('action', models.CharField(max_length=100, verbose_name='действие')),
                ('is_pleasurable', models.BooleanField(default=False, verbose_name='Признак приятной привычки')),
                ('frequency', models.IntegerField(choices=[(1, 'Ежедневная'), (3, 'Трехдневная'), (7, 'Еженедельная')], default=1, verbose_name='периодичность')),
                ('reward', models.CharField(max_length=255, verbose_name='Вознаграждение')),
                ('time_to_perform', models.TimeField(verbose_name='Время на выполнение')),
                ('is_public', models.BooleanField(default=False, verbose_name='Признак публичности')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habit.habit', verbose_name='Связанная привычка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='создатель')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]