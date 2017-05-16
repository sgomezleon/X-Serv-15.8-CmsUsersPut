from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from cmsuserput.models import Pages
# Create your views here.

@csrf_exempt
def home(request):

	if request.user.is_authenticated():
		respuesta = "<br>Logedd in as " + request.user.username + ". <a href='/logout'>Logout</a>"
	else:
		respuesta = "<br>Not logged in. <a href='/admin'> Login</a>"
		
		lista_paginas = Pages.objects.all()
		respuesta += "<h3>Lista de paginas</h3>"
		for pagina in lista_paginas:
			respuesta += "<br><a href='" + pagina.nombre +"'>" + pagina.nombre + "</br>"
		return HttpResponse(respuesta)
	
	if request.method == 'GET':	
		
		respuesta = "<br>Logedd in as " + request.user.username + ". <a href='/logout'>Logout</a>"
		
		respuesta += "<h1>Bienvenidos</h1>"
		respuesta += """
					<form action="" method='post'" 
					<br>Escribe un nombre: <input type='text' name='nombre' value="" ></br>
					<br>Escribe una pagina: <input type='text' name='pagina' value=""></br>
					<input type='submit' value='Enviar'>
					"""
		
		lista_paginas = Pages.objects.all()
		respuesta += "<h3>Lista de paginas</h3>"
		for pagina in lista_paginas:
			respuesta += "<br><a href='" + pagina.nombre +"'>" + pagina.nombre + "</br>"
		return HttpResponse(respuesta)

	elif request.method == 'POST':
		nombre = request.POST['nombre']	
		pagina = request.POST['pagina']
		pag = Pages(nombre = nombre, pagina = pagina)
		pag.save()
		return redirect("/")
		
	elif request.method == 'PUT':
		body = request.body.decode('utf-8')
		nombre,pagina = body.split(",")
		pag = Pages(nombre = nombre, pagina = pagina)
		pag.save()
		return redirect("/")
	else:
		respuesta = "Method not valid"
		return HttpResponse(respuesta)

def nombre_pagina(request,nombre):
	try:
		pagina = Pages.objects.get(nombre = nombre)
		respuesta = pagina.pagina
	except Pages.DoesNotExist:
		respuesta = "pagina no encontrada"
	return HttpResponse(respuesta)
	

