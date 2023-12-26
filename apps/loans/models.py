from django.db import models

# aseguradora


class Insurier(models.Model):
    # esta
    id = models.IntegerField(
        verbose_name="id", primary_key=True, unique=True, auto_created=True)
    name = models.CharField(verbose_name="aseguradora", max_length=20)

# rubro


class Entry(models.Model):
    ID = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10, verbose_name='código', unique=True)
    description = models.TextField(verbose_name='descripción')
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='valor')


# seguro


class Insurance(models.Model):
    id = models.IntegerField(
        verbose_name="id", primary_key=True, unique=True, auto_created=True)
    insurier = models.ForeignKey(Insurier, on_delete=models.CASCADE)
    date = models.DateField(verbose_name="fecha", auto_now=True)
    pass
# empleado

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, verbose_name='nombre')
    lastname = models.CharField(max_length=40, verbose_name='apellido')
    identity_card = models.CharField(max_length=10, unique=True, verbose_name='cédula')
    position = models.CharField(max_length=50, verbose_name='cargo')
    department = models.CharField(max_length=50, verbose_name='departamento')
    date_entry = models.DateField(verbose_name='fecha de ingreso')

    def __str__(self):
        return f"{self.name} {self.lastname} - {self.position}"

