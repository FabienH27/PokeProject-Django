# Generated by Django 3.1.6 on 2021-03-04 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('default_front_sprite_url', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('pokedex_number', models.IntegerField()),
                ('default_back_sprite_url', models.CharField(blank=True, max_length=255, null=True)),
                ('front_shiny_sprite_url', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'pokemons',
            },
        ),
        migrations.CreateModel(
            name='PokemonStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemons.pokemon')),
            ],
            options={
                'db_table': 'pokemon_stats',
            },
        ),
        migrations.CreateModel(
            name='PokemonType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemons.pokemon')),
            ],
            options={
                'db_table': 'pokemon_types',
            },
        ),
        migrations.CreateModel(
            name='UserPokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemons.pokemon')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_pokemons',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('pokemons', models.ManyToManyField(related_name='type', through='pokemons.PokemonType', to='pokemons.Pokemon')),
            ],
            options={
                'db_table': 'types',
            },
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('pokemons', models.ManyToManyField(related_name='stat', through='pokemons.PokemonStat', to='pokemons.Pokemon')),
            ],
            options={
                'db_table': 'stat',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='pokemontype',
            name='types',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemons.type'),
        ),
        migrations.AddField(
            model_name='pokemonstat',
            name='stat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemons.stat'),
        ),
    ]
