from django.db import models

# aseguradora


class Insurier(models.Model):
    # esta
    id = models.AutoField(
        primary_key=True)
    name = models.CharField(verbose_name="aseguradora", max_length=20)

    def __str__(self):
        return (f"{self.name}")


# rubro
ESTADO_CHOICES = [
    ('activo', 'Activo'),
    ('inactivo', 'Inactivo'),
]

class Entry(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(verbose_name='descripción', null=True)
    value = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='valor', null=True)
    state = models.CharField(max_length=20, 
        verbose_name='estado', choices=ESTADO_CHOICES, default='activo')
    num_cuotas = models.IntegerField(verbose_name='número de cuotas', blank=True, null=True)
    cuota = models.DecimalField(max_digits=10, decimal_places=2, 
        verbose_name='cuota', blank=True, null=True)

    def __str__(self):
        return (f"{self.code} {self.id} {self.value}")
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.saldo = self.value
        if self.num_cuotas:
            self.cuota = self.value / self.numero_cuotas
        super(Entry, self).save(*args, **kwargs)

# seguro

# empleado



class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, verbose_name='nombre', default='')
    lastname = models.CharField(
        max_length=40, verbose_name='apellido', null=True, default='')
    identity_card = models.CharField(
        max_length=10, unique=True, verbose_name='cédula', default='')
    position = models.CharField(
        max_length=50, verbose_name='cargo', default='')
    department = models.CharField(
        verbose_name='departamento', max_length=50, null=True, default='')
    date_entry = models.DateField(
        verbose_name='fecha de ingreso', auto_now=True)
    state = models.CharField(max_length=20, 
        verbose_name='estado', choices=ESTADO_CHOICES, default='activo')

    def __str__(self):
        return f"{self.name} {self.lastname}"


class Insurance(models.Model):
    id = models.AutoField(primary_key=True)
    insurier = models.ForeignKey(Insurier, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    date = models.DateField(verbose_name="fecha", auto_now=True)

    def __str__(self):
        return (f"{self.date} {self.id} {self.insurier} {self.employee}")
