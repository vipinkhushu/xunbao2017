from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import player,question


def index(request,pk):
	try:
		player1=player.objects.get(fb_id=pk)
	except player.DoesNotExist:
		player1=player.objects.create(fb_id=pk,name="sameer")
		player1.save()
	level =player1.level
	que=question.objects.get(level=level)
	des = que.description
	sr = player1.pk
	return HttpResponse("yes")

def check(request,pk,ans):
	try:
		player1=player.objects.get(fb_id=pk)
	except player.DoesNotExist:
		player1=player.objects.create(fb_id=pk,name="sameer")
		player1.save()
	level =player1.level
	que=question.objects.get(level=level)
	if ans==que.answer:
		player1.levelup()
		player1.save()
		return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')

def ranks(request):
	players = player.objects.order_by('-level','created_on')
	return render(request,'index.html',{'all':players})
