from django.db import models
from ftplib import FTP

class Conecta(object):
	"""docstring for Conecta"""
	def __init__(self):
		self.url = "127.0.0.1"
		self.porta = 2121
		self.urldown = "/home/diego/Downloads/"
		self.handler = FTP()
		self.handler.connect(self.url, self.porta)
		self.handler.login()
		
	def list(self):
		lista = []
		a = self.handler.nlst()
		for f in a:
			lista.append(f)
		return lista

	def download(self, file):
		Dfile = open(self.urldown + file, 'wb')
		self.handler.retrbinary('RETR ' + file, Dfile.write)
		Dfile.close()
		return True

	# def upload(self, file):
	# 	self.handler.storbinary('STOR ' + str(file), open(file, 'rb'), 1024)
	# 	return True
		