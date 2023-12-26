from django.db import models

# aseguradora


class Insurier(models.Model):
    # esta
    id = models.IntegerField(
        verbose_name="id", primary_key=True, unique=True, auto_created=True)
    name = models.CharField(verbose_name="aseguradora", max_length=20)

# rubro


class Entry(models.Model):
    id = models.IntegerField(
        verbose_name='id', primary_key=True, unique=True, auto_created=True)
    code = models.CharField(
        max_length=10, verbose_name='código', unique=True, null=True)
    description = models.TextField(verbose_name='descripción', null=True)
    value = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='valor', null=True)


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
    name = models.CharField(max_length=40, verbose_name='nombre', default='')
    lastname = models.CharField(
        max_length=40, verbose_name='apellido', null=False, default='')
    identity_card = models.CharField(
        max_length=10, unique=True, verbose_name='cédula', default='')
    position = models.CharField(
        max_length=50, verbose_name='cargo', default='')
    department = models.CharField(
        verbose_name='departamento', max_length=50, null=False, default='')
    date_entry = models.DateField(
        verbose_name='fecha de ingreso', auto_now=True)

    def __str__(self):
        return f"{self.name} {self.lastname} - {self.position}"
