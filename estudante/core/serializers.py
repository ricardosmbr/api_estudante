from rest_framework import serializers
from .models import Estudante

class EstudanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estudante
        fields = ('id','nome', 'telefone' ,'curso','create_at','update_at')

