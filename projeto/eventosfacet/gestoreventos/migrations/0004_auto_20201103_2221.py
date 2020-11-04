# Generated by Django 3.1.3 on 2020-11-04 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestoreventos', '0003_funcionario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Palestrante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_palestrante', models.CharField(max_length=150)),
                ('data_nascimento', models.DateField()),
                ('cpf', models.CharField(max_length=11)),
                ('email_palestrante', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='curso_organizador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='gestoreventos.curso'),
        ),
        migrations.AddField(
            model_name='evento',
            name='data_final',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='evento',
            name='data_inicio',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='evento',
            name='organizador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='gestoreventos.funcionario'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='curso_vinculado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='gestoreventos.curso'),
        ),
        migrations.AddField(
            model_name='evento',
            name='palestrantes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='gestoreventos.palestrante'),
        ),
    ]
