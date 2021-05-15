# Generated by Django 3.1 on 2021-05-15 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Euro', max_length=48)),
                ('code', models.CharField(default='EUR', max_length=3)),
                ('symbol', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name': 'currency',
                'verbose_name_plural': 'currencies',
                'db_table': 'currency',
            },
        ),
        migrations.CreateModel(
            name='DSR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=256)),
                ('period_end', models.DateField()),
                ('period_start', models.DateField()),
                ('status', models.CharField(choices=[('ingested', 'INGESTED'), ('failed', 'FAILED')], default='ingested', max_length=48)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dsrs', to='dsrs.currency')),
            ],
            options={
                'verbose_name': 'dsr',
                'verbose_name_plural': 'dsrs',
                'db_table': 'dsr',
            },
        ),
        migrations.CreateModel(
            name='Territory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Spain', max_length=48)),
                ('code_2', models.CharField(default='ES', max_length=2)),
                ('code_3', models.CharField(max_length=3)),
                ('local_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='territories', to='dsrs.currency')),
            ],
            options={
                'verbose_name': 'territory',
                'verbose_name_plural': 'territories',
                'db_table': 'territory',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dsp_id', models.CharField(max_length=256)),
                ('usages', models.IntegerField(default=0)),
                ('revenue', models.BigIntegerField(default=0)),
                ('isrc', models.CharField(blank=True, max_length=256, null=True)),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('artists', models.CharField(blank=True, max_length=256, null=True)),
                ('dsrs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resource', to='dsrs.dsr')),
            ],
            options={
                'verbose_name': 'resource',
                'verbose_name_plural': 'resources',
                'db_table': 'resource',
            },
        ),
        migrations.AddField(
            model_name='dsr',
            name='territory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dsrs', to='dsrs.territory'),
        ),
    ]
