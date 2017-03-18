from main.models import player,question,message,logs
from rest_framework.generics import RetrieveAPIView,ListAPIView

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status

from.serializers import QueSerializer,messageSerializer,rankserializer
from datetime import datetime

class QueDetailView(ListAPIView):
	serializer_class = QueSerializer
	def get_queryset(self,*args,**kwargs):
		try:
			player1= player.objects.get(fb_id=self.kwargs['pk'])
		except player.DoesNotExist:
			player1 = player.objects.create(fb_id=self.kwargs['pk'],name=self.kwargs['name'])
			player1.save()
		print (player1.name,player1.level)
		queryset_list=question.objects.filter(level=player1.level)
		print (queryset_list)
		return queryset_list

class QueDetail(APIView):
	def post(self, request, format=None):
		if request.data.get('fb_id')=="" or request.data.get('name')=="" or request.data.get('email_xid')=="" :
			data ={'description':"",
			'level':1,
			'id':0}
			print ("yes")
			serializer = QueSerializer(data=data)
			if serializer.is_valid():
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		try :
			player1 = player.objects.get(fb_id = request.data.get('fb_id'))
		except player.DoesNotExist:
			player1 = player.objects.create(fb_id =request.data.get('fb_id'),name=request.data.get('name') ,email_id=request.data.get('email_id'))
			player1.save()
		print (player1.name,player1.email_id,player1.level)
		que = question.objects.get(level=player1.level) 
		data ={'description':que.description,
		'level':que.level,
		'id':que.id}
		serializer = QueSerializer(data=data)
		if serializer.is_valid():
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class check(APIView):
	def post(self,request,format=None):
		if request.data.get('fb_id')=="" or request.data.get('name')=="" or request.data.get('answer')=="" :
			data ={'message':"fields missing !!",
			'flag':0}
			serializer = messageSerializer(data=data)
			if serializer.is_valid():
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		try:
			player1 = player.objects.get(fb_id=request.data.get('fb_id'),name=request.data.get('name'))
		except player.DoesNotExist:
			data ={'message':"User Doesnot exist !!",
			'flag':0}
			serializer = messageSerializer(data=data)
			if serializer.is_valid():
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		log =logs.objects.create(fb_id=request.data.get('fb_id'),name=request.data.get('name'),level=player1.level,answer=request.data.get('answer'))
		log.save()
		
		que =question.objects.get(level=player1.level)
		if que.answer.lower().strip() == request.data.get('answer').lower().strip():
			player1.levelup()
			player1.created_on = datetime.now()
			player1.save()
			data ={'message':"success",
			'flag':1,}
			serializer = messageSerializer(data=data)
			if serializer.is_valid():
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		else:
			data ={'message':"Incorrect Answer ",
			'flag':0,}
			serializer = messageSerializer(data=data)
			if serializer.is_valid():
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ranklist(ListAPIView):
	queryset = player.objects.order_by('-level','created_on')
	serializer_class = rankserializer


class check1(ListAPIView):
	serializer_class = messageSerializer
	def get_queryset(self,*args,**kwargs):
		player1= player.objects.get(fb_id=self.kwargs['pk'])
		print (player1.name,player1.level)
		queryset_list=question.objects.get(level=player1.level)
		if queryset_list.answer==self.kwargs['ans']:
			player1.levelup()
			player1.save()
			return message.objects.filter(flag=1)
		else :
			return message.objects.filter(flag=0)
