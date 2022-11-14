# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Empleados(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    foto = models.CharField(max_length=200)
    cargo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empleados'


class Platos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    fotografia = models.CharField(max_length=200)
    precio = models.IntegerField()
    tipo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'platos'
