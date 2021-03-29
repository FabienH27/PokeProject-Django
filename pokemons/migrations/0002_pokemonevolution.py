# Generated by Django 3.1.6 on 2021-03-17 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonEvolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemonEvolution1', models.CharField(max_length=255)),
                ('pokemonEvolution2', models.CharField(max_length=255)),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemons.pokemon')),
            ],
            options={
                'db_table': 'pokemon_evolution',
            },
        ),
    ]