from django.db import models

# Create your models here.
class jurisprudencias(models.Model):
    id                  = models.AutoField(primary_key=True)
    id_jurisprudencias  = models.IntegerField()
    tipoCausa           = models.CharField(max_length=255)
    rol                 = models.CharField(max_length=255)
    caratula            = models.CharField(max_length=255)
    nombreProyecto      = models.CharField(max_length=255)
    fechaSentencia      = models.DateField()
    descriptores        = models.TextField()
    linkSentencia       = models.CharField(max_length=255)
    urlSentencia        = models.CharField(max_length=255)
    activo              = models.BooleanField()
    tribunal            = models.CharField(max_length=255)
    valores             = models.TextField()
    tipo                = models.CharField(max_length=255)
    relacionada         = models.CharField(max_length=255)
    visitas             = models.IntegerField()