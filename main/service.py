from django.http import JsonResponse
import requests
import pandas as pd
from bs4 import BeautifulSoup
import json


def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_username(params={}):
    response = generate_request('https://serpapi.com/searches/f2f2618f7a907b4d/622faa3ac47d3c6f6b3416bc.json', params)
    
    if response:

       equipos = response['knowledge_graph']['jugadores']
    
       return equipos
    
    return ''


def scrap():
    url = 'https://argentina.as.com/resultados/futbol/copa_liga_argentina/clasificacion/'

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    #Equipos
    eq = soup.find_all('span', class_='nombre-equipo')
    pt = soup.find_all('td', class_='destacado')
    
    url_velez = 'https://velez.com.ar/futbol/estadisticas'
  
    url_link = requests.get(url_velez) 
    file = BeautifulSoup(url_link.content, 'html.parser') 
  
    find_table = file.find('table', class_='table table-bordered table-hover text-center') 
    rows = find_table.find_all('tr') 
    est = list()
    count = 0
    for i in rows: 
        table_data = i.find_all('td')
        data = [j.text for j in table_data] 
        est.append(data)

    posiciones = list()
    
    count = 14
    i = 1
    while count < 28:
        
        signer_json = {}
        signer_json['nombre'] = eq[count].text
        signer_json['puntos'] = pt[count].text
        signer_json['pj'] = est[i][2]
        signer_json['g'] = est[i][3]
        signer_json['e'] = est[i][4]
        signer_json['p'] = est[i][5]
        signer_json['gf'] = est[i][6]
        signer_json['gc'] = est[i][7]
        signer_json['dif'] = est[i][8]
        posiciones.append(signer_json)
        i +=1
        count += 1

    return posiciones

# def prueba():
#     URL = 'https://velez.com.ar/futbol/estadisticas'
  
#     url_link = requests.get(URL) 
#     file = BeautifulSoup(url_link.content, 'html.parser') 
  
#     find_table = file.find('table', class_='table table-bordered table-hover text-center') 
#     rows = find_table.find_all('tr') 
#     est = list()
    
#     for i in rows: 
#         table_data = i.find_all('td')
#         data = [j.text for j in table_data] 
#         est.append(data)
#         # for j in table_data:
#         #     est.append(j.text)


#     datos = list()  
    
#     i = 1
#     while i < 15:
            
#         signer_json = {}
       
#         signer_json['pts'] = est[i][1]
#         signer_json['pj'] = est[i][2]
#         signer_json['g'] = est[i][3]
#         signer_json['e'] = est[i][4]
#         signer_json['p'] = est[i][5]
#         signer_json['gf'] = est[i][6]
#         signer_json['gc'] = est[i][7]
#         signer_json['dif'] = est[i][8]
#         datos.append(signer_json)
#         i += 1

#     return datos
  