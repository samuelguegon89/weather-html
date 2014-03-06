#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import requests
import json
from jinja2 import Template
import webbrowser


plantilla = open("plantilla.html","r")
contador=0
provincias = ["Almeria","Cadiz","Cordoba","Huelva","Jaen","Malaga","Sevilla"]
temperaturamin=[]
temperaturamax=[]
vientos=[]
direccion=[]
valor =""

html = ''
for linea in plantilla:
	html += linea
	
plantilla= Template(html)

 
while contador!=7:
	
	respuesta=requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,Spain' % provincias[contador]})
	dicc=json.loads(respuesta.text)
	temperaturamin1=dicc["main"]["temp_min"] -273
	temperaturamax1=dicc["main"]["temp_max"] -273
	vientos1=dicc["wind"]["speed"]
	direccion1=dicc["wind"]["deg"]
	
	if (direccion1 >= 337.5 and direccion1<=360) or (direccion1 >= 0 and direccion1<=22.5):
		valor='N'
	if direccion1 >22.5 and direccion1<67.5:
		valor='N.E'
	if direccion1 >=67.5 and direccion1<=112.5:
		valor='E'
	if direccion1 >112.5 and direccion1<157.5:
		valor='S.E'
	if direccion1 >=157.5 and direccion1<=202.5:
		valor='S'
	if direccion1 >202.5 and direccion1<247.5:
		valor='S.O'
	if direccion1 >=247.5 and direccion1<=292.5:
		valor='O'
	if direccion1 >292.5 and direccion1<337.5:
		valor='N.O'
	
	temperaturamin.append(temperaturamin1)
	temperaturamax.append(temperaturamax1)
	vientos.append(vientos1)
	direccion.append(valor)
	
	contador=contador+1
	
plantilla = plantilla.render(provincias=provincias,temperatura_max=temperaturamax,temperatura_min=temperaturamin,velocidad_viento=vientos,direccion=direccion)
abrir=open('salida.html','w')
abrir.write(plantilla)
webbrowser.open('salida.html')

