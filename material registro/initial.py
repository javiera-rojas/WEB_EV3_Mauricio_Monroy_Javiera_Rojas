from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('ISBN', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('Nombre del libro', models.CharField(max_length=20, verbose_name='')),
                ('Autor', models.CharField(max_length=30)),
                ('Descripción', models.CharField( max_length=200)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]
