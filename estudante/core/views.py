from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from . models import Estudante
from . serializers import EstudanteSerializer
import requests

@api_view(['GET'])
def home(request):
	urls ={}
	base = "http://127.0.0.1:8000/"
	urls['Listar Estudantes'] = base+"estudante/"
	urls['Adicionar Estudantes'] = base+"addestudante/"
	return Response(urls)

@api_view(['GET'])
def ListarEstudanteView(request):
	if request.method == 'GET':
		obj = Estudante.objects.all()
		dados = request.query_params
		for item in dados:
			obj=""
			if(item == "id"):
				obj = Estudante.objects.filter(pk=dados["id"])
		serializer = EstudanteSerializer(obj, many=True)
		return Response(serializer.data)

@api_view(['POST'])
def AdicionarEstudanteView(request):
	if request.method == 'POST':
		texto =''
		if(isinstance(request.data, str)):
			dados = eval(request.data)
		else:
			dados = request.data
		obj = Estudante.objects.all()
		#verifica json simples ou lista
		if (isinstance(request.data, dict)):
			serializer = EstudanteSerializer(data=dados)
			if serializer.is_valid():
				serializer.save()
			else:
				texto = str(serializer.errors)
				print(texto)
		else:
			serializer = EstudanteSerializer(data=dados,many=True)
			if serializer.is_valid():
				serializer.save()
			else:
				texto = str(serializer.errors)	
				print(texto)		

	return Response(serializer.data)