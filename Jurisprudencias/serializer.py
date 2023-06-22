from rest_framework import serializers
from .models import Jurisprudencias

class JurisprudenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jurisprudencias
        fields = ('id', 'id_jurisprudencias','tipoCausa','rol','caratula','nombreProyecto','fechaSentencia','descriptores','linkSentencia','urlSentencia','activo','tribunal','valores','tipo','relacionada','visitas')