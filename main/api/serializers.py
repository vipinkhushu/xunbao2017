from rest_framework.serializers import ModelSerializer

from main.models import question,player,message

class QueSerializer(ModelSerializer):
	class Meta:
		model = question
		fields = [
		'description',
		'level',
		'id',
		]

class messageSerializer(ModelSerializer):
	class Meta:
		model = message
		fields = [
		'message',
		'flag',
		]

class rankserializer(ModelSerializer):
	class Meta:
		model = player
		fields = [
		'name',
		'level',
		]