from django.db import models

# aseguradora


class Insurier(models.Model):
    # esta
    id = models.IntegerField(
        verbose_name="id", primary_key=True, unique=True, auto_created=True)
    name = models.CharField(verbose_name="aseguradora", max_length=20)

# rubro


class entry(models.Model):
    # esta
    pass

# seguro


class Insurance(models.Model):
    id = models.IntegerField(
        verbose_name="id", primary_key=True, unique=True, auto_created=True)
    insurier = models.ForeignKey(Insurier, on_delete=models.CASCADE)
    date = models.DateField(verbose_name="fecha", auto_now=True)
    pass
# empleado


class employee(models.Model):
    pass
