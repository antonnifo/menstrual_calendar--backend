# Generated by Django 5.1.1 on 2025-01-30 12:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cycles', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodFlowLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('flow_level', models.CharField(blank=True, choices=[('none', 'None'), ('light', 'Light'), ('spotting', 'Spotting'), ('medium', 'Medium'), ('heavy', 'Heavy'), ('very_heavy', 'Very Heavy')], max_length=20, null=True)),
                ('cycle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cycles.cycles')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MedicationLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('medication', models.CharField(blank=True, choices=[('birth_control', 'Birth Control Pills'), ('depo_shot', 'Depo-Provera Shot'), ('hormone_therapy', 'Hormone Therapy'), ('fertility_drugs', 'Fertility Drugs'), ('pain_relief', 'Pain Relief (e.g., Ibuprofen)'), ('pcos_medication', 'PCOS Medication'), ('thyroid_medication', 'Thyroid Medication'), ('antidepressants', 'Antidepressants'), ('antibiotics', 'Antibiotics')], max_length=100, null=True)),
                ('cycle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cycles.cycles')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MoodLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('mood', models.CharField(blank=True, choices=[('happy', 'Happy'), ('energized', 'Energized'), ('confident', 'Confident'), ('optimistic', 'Optimistic'), ('relaxed', 'Relaxed'), ('focused', 'Focused'), ('sociable', 'Sociable'), ('irritable', 'Irritable'), ('anxious', 'Anxious'), ('sad', 'Sad'), ('depressed', 'Depressed'), ('fatigued', 'Fatigued'), ('stressed', 'Stressed'), ('restless', 'Restless')], max_length=50, null=True)),
                ('cycle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cycles.cycles')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SexualIntercourseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('protection_used', models.CharField(blank=True, choices=[('protected', 'Protected'), ('unprotected', 'Unprotected')], default=False, max_length=20, null=True)),
                ('cycle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cycles.cycles')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SymptomLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('symptom', models.CharField(blank=True, choices=[('cramps', 'Cramps'), ('low_energy', 'Low Energy'), ('mood_swings', 'Mood Swings'), ('increased_energy', 'Increased Energy'), ('clearer_skin', 'Clearer Skin'), ('clear_cervical_mucus', 'Clear Cervical Mucus'), ('egg_white_cervical_mucus', 'Egg White Cervical Mucus'), ('increased_libido', 'Increased Libido'), ('bbt_rise', 'Basal Body Temperature Rise'), ('cravings', 'Cravings'), ('bloating', 'Bloating'), ('acne', 'Acne')], max_length=100, null=True)),
                ('cycle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cycles.cycles')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
