from django.db import models

ESTADO_CHOICES = [
    ('activo', 'Activo'),
    ('inactivo', 'Inactivo'),
]

# aseguradora


class Insurier(models.Model):
    id = models.AutoField(
        primary_key=True)
    name = models.CharField(verbose_name="aseguradora", max_length=20)
    tlf_contact = models.CharField(
        verbose_name="tlf_contacto", max_length=10, default="")
    state = models.CharField(max_length=20,
                             verbose_name='estado',
                             choices=ESTADO_CHOICES,
                             default='activo')

    def __str__(self):
        return (f"{self.name}")
# empleado


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, verbose_name='nombre', default='')
    lastname = models.CharField(
        max_length=40, verbose_name='apellido', null=True, default='')
    identity_card = models.CharField(
        max_length=10, unique=True, verbose_name='cédula', default='')
    cargas = models.IntegerField(verbose_name='cargas', default=0)
    position = models.CharField(
        max_length=50, verbose_name='cargo', default='')
    department = models.CharField(
        verbose_name='departamento', max_length=50, null=True, default='')
    date_entry = models.DateField(
        verbose_name='fecha de ingreso', auto_now=True)
    state = models.CharField(max_length=20,
                             verbose_name='estado',
                             choices=ESTADO_CHOICES,
                             default='activo')

    def employee(self):
        return f"{self.name} {self.lastname}"


# TODO: detalle seguro
# class det_insurance(models.Model):
#     id = models.AutoField(primary_key=True)
#     employee = models.ForeignKey(Employee,
#                                  on_delete=models.CASCADE,
#                                  null=True)

# seguro


class Insurance(models.Model):
    id = models.AutoField(primary_key=True)
    insurier = models.ForeignKey(Insurier, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    date = models.DateField(verbose_name="fecha", auto_now=True)
    state = models.CharField(max_length=20,
                             verbose_name='estado',
                             choices=ESTADO_CHOICES,
                             default='activo')
    # TODO:
    # det_insurance = models.ForeignKey(det_insurance,
    #                                   on_delete=models.PROTECT)

    def __str__(self):
        return (f"{self.date} {self.id} {self.insurier}")


# rubro


class Entry(models.Model):
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    description = models.TextField(verbose_name='descripción',
                                   null=True)
    code = models.CharField(verbose_name='codigo',
                            max_length=20,
                            default='')
    value = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name='valor',
                                null=True)
    state = models.CharField(max_length=20,
                             verbose_name='estado',
                             choices=ESTADO_CHOICES,
                             default='activo')

    def __str__(self):
        return (f"{self.code} {self.value}")
    # employee = models.ForeignKey(Employee,
    #                              on_delete=models.CASCADE,
    #                              null=True)
    # num_cuotas = models.IntegerField(
    #     verbose_name='número de cuotas', blank=True, null=True)
    # # valor de la cuota
    # cuota = models.DecimalField(max_digits=10, decimal_places=2,
    #                             verbose_name='cuota', blank=True, null=True)
    #
    # def __str__(self):
    #     return (f"{self.code} {self.id} {self.value}")
    #
    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.saldo = self.value
    #     if self.num_cuotas:
    #         self.cuota = self.value / self.num_cuotas
    #     super(Entry, self).save(*args, **kwargs)

# cuota


class Fee(models.Model):
    id = models.AutoField(primary_key=True)
    payment_date = models.DateField(
        verbose_name="fecha de pago",
        null=True)

# pagos realizados


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    payment_date = models.DateField(
        verbose_name="fecha de pago",
        auto_now=True)
    amount = models.FloatField(verbose_name="cantidad",
                               default=0)
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
