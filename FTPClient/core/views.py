from django.shortcuts import render, redirect
from .models import Conecta
from django.http import Http404

def index(request):
	conexao = Conecta()
	return render(request, "core/index.html", {
		'lista':conexao.list(),
		'con':conexao,
		})

def baixar(request, file):
	conexao = Conecta()
	if file not in conexao.list():
		raise Http404
	conexao.download(file)
	return redirect("/")

#em construção
def upload(request):
	if request.method == 'POST':
		arquivo = request.FILES['file']
		#file = open(arquivo,'rb')
		conexao = Conecta()
		print(dir(arquivo))
		print(arquivo.file)
		conexao.upload(arquivo)
		return redirect("/")
	return render(request, "core/upload.html")