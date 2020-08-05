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
	urls['Autera Estudantes'] = base+"autestudante/"
	urls['Apaga Estudantes'] = base+"apaestudante/"
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

		#verifica json simples ou lista
		if (isinstance(request.data, dict)):
			serializer = EstudanteSerializer(data=dados)
			if serializer.is_valid():
				serializer.save()
			else:
				return Response(serializer.errors)

		else:
			serializer = EstudanteSerializer(data=dados,many=True)
			if serializer.is_valid():
				serializer.save()
			else:
				return Response(serializer.errors)		

	return Response(serializer.data)

@api_view(['POST'])
def AuterarEstudanteView(request):
	if request.method == 'POST':
		#verifica json simples ou lista
		if (isinstance(request.data, list)):
			return Response('formato json: invalido ')
		dados = request.data
		ide = request.data['id']
		print("id ", ide)
		try:
			obj = Estudante.objects.get(pk=ide)
		except Exception as e:
			return Response('id: invalido ')		
		serializer = EstudanteSerializer(obj,data=dados)
		if serializer.is_valid():
			serializer.save()
		else:
			return Response(serializer.errors)

	return Response(serializer.data)

@api_view(['POST'])
def ApagaEstudanteView(request):
	if request.method == 'POST':
		#verifica json simples ou lista
		if (isinstance(request.data, list)):
			return Response('formato json: invalido ')
		dados = request.data
		try:
			ide = request.data['id']
			obj = Estudante.objects.get(pk=ide)
		except Exception as e:
			return Response('id: invalido ')		
		try:
			obj.delete
		except Exception as e:
			return Response('id: invalido ')

	return Response('id: apagado ')