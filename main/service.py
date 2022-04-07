#from datetime import datetime
from re import T
import requests
import pandas as pd
from bs4 import BeautifulSoup
import json
import datetime


def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

# def get_username(params={}):
#     response = generate_request('https://serpapi.com/searches/f2f2618f7a907b4d/622faa3ac47d3c6f6b3416bc.json', params)
    
#     if response:

#        equipos = response['knowledge_graph']['jugadores']
    
#        return equipos
    
#     return ''

def get_username(params={}):
    
    response = generate_request('https://site.web.api.espn.com/apis/site/v2/sports/soccer/ARG.COPA_LPF/teams/21/roster?region=ar&lang=es&contentorigin=deportes&limit=99', params)
    player = {}

    if response:
        
        arquero = jugador(response, 'Arquero')

        player['arquero'] = arquero

        defensor = jugador(response, 'Defensor')

        player['defensa'] = defensor
        
        medio = jugador(response, 'Mediocampista')

        player['medio'] = medio

        atacante = jugador(response, 'Atacante')

        player['ataque'] = atacante


        return player

    return ''

def jugador(response, posicion):

        resultado = list()

        equipos = response['athletes']
       
        for n in equipos:
            
            if n['position']['displayName'] == posicion:
                tablaProsiciones = {}
                tablaProsiciones['nombre'] = n['fullName']
                tablaProsiciones['edad'] = n['age']
                tablaProsiciones['altura'] = n['displayHeight']
                tablaProsiciones['pos'] = n['position']['abbreviation']
                tablaProsiciones['peso'] = n['displayWeight']
                tablaProsiciones['nac'] = n['citizenship']
                resultado.append(tablaProsiciones)
                
        return resultado
    
    


# def resultados(params={}):
#     response = generate_request('https://serpapi.com/search.json?engine=google&q=resultados+velez+sarsfield&location=Mexico&google_domain=google.com.mx&gl=mx&hl=es&api_key=380a1822a2d4935cffd76013b3b82740ee1ae43ee801bc0690edf4d5b916c0c5', params)
    
#     if response:

#        fixture = response['sports_results']['games']
       
#        return fixture
    
#     return ''


def resultados(params={}):
    response = generate_request('https://site.web.api.espn.com/apis/site/v2/sports/soccer/all/teams/21/schedule?region=ar&lang=es&season=2022', params)
    
    resultado = list()

    i = 1
    if response:

        fixture = response['events']
        
        for c in fixture:
            if c['id'] != '625787':
                for e in c['competitions']:
                    fecha = e['date']
                    dia = datetime.datetime.strptime(fecha, '%Y-%m-%dT%H:%MZ').strftime('%A')
                    fecha1 = datetime.datetime.strptime(fecha, '%Y-%m-%dT%H:%MZ').strftime("%d-%m-%Y")
                    
                    
                    #for l in e['competitors']:
                        
                    tablaProsiciones = {}
                    tablaProsiciones['dia'] = dia
                    tablaProsiciones['fecha'] = fecha1
                    tablaProsiciones['equipo1'] = e['competitors'][0]['team']['displayName']
                    tablaProsiciones['equipo2'] = e['competitors'][1]['team']['displayName']
                    tablaProsiciones['logo1'] = e['competitors'][0]['team']['logos'][0]
                    tablaProsiciones['logo2'] = e['competitors'][1]['team']['logos'][0]
                    tablaProsiciones['score1'] = e['competitors'][0]['score']['value']
                    tablaProsiciones['score2'] = e['competitors'][1]['score']['value']
                    

                    resultado.append(tablaProsiciones)
                        
                        # i +=1
                        # if i == 6:
                        #     break
         
        return resultado
    
    return ''


def calendario(params={}):
    response = generate_request('https://site.web.api.espn.com/apis/site/v2/sports/soccer/all/teams/21/schedule?region=ar&lang=es&fixture=true', params)
    
    resultado = list()

    i = 1
    if response:

        fixture = response['events']
        
        for c in fixture:
            calendario = {}
            calendario['liga'] = c['league']['abbreviation']
            for e in c['competitions']:
                
                fecha = e['date']
                    
                fecha1 = datetime.datetime.strptime(fecha, '%Y-%m-%dT%H:%MZ').strftime("%d-%m")
                       
                
                calendario['fecha'] = fecha1
                calendario['equipo1'] = e['competitors'][0]['team']['displayName']
                calendario['equipo2'] = e['competitors'][1]['team']['displayName']
                calendario['logo1'] = e['competitors'][0]['team']['logos'][0]
                calendario['logo2'] = e['competitors'][1]['team']['logos'][0]
                

                resultado.append(calendario)
                        
                        
         
        return resultado
    
    return ''


# def scrap():
#     url = 'https://argentina.as.com/resultados/futbol/copa_liga_argentina/clasificacion/'

#     page = requests.get(url)

#     soup = BeautifulSoup(page.content, 'html.parser')

#     #Equipos
#     eq = soup.find_all('span', class_='nombre-equipo')
#     pt = soup.find_all('td', class_='destacado')
    
#     url_velez = 'https://velez.com.ar/futbol/estadisticas'
  
#     url_link = requests.get(url_velez) 
#     file = BeautifulSoup(url_link.content, 'html.parser') 
  
#     find_table = file.find('table', class_='table table-bordered table-hover text-center') 
#     rows = find_table.find_all('tr') 
#     est = list()
#     count = 0
#     for i in rows: 
#         table_data = i.find_all('td')
#         data = [j.text for j in table_data] 
#         est.append(data)

#     posiciones = list()
    
#     count = 14
#     i = 1
#     while count < 28:
        
#         tablaProsiciones = {}
#         tablaProsiciones['puesto'] = i
#         tablaProsiciones['nombre'] = eq[count].text
#         tablaProsiciones['puntos'] = pt[count].text
#         tablaProsiciones['pj'] = est[i][2]
#         tablaProsiciones['g'] = est[i][3]
#         tablaProsiciones['e'] = est[i][4]
#         tablaProsiciones['p'] = est[i][5]
#         tablaProsiciones['gf'] = est[i][6]
#         tablaProsiciones['gc'] = est[i][7]
#         tablaProsiciones['dif'] = est[i][8]
#         posiciones.append(tablaProsiciones)
#         i +=1
#         count += 1

#     return posiciones

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
  
def tabla(params={}):
    response = generate_request('https://site.web.api.espn.com/apis/v2/sports/soccer/arg.copa_lpf/standings?region=ar&lang=es&contentorigin=deportes&season=2022&sort=rank%3Aasc', params)
                               
    if response:
        
        fixture = response['children']
        i = 1
        datos = list() 
        for t in fixture:
        
            if t['id'] == "2":
                #return  t['standings']['entries']
                for s in t['standings']['entries']:
            
                    tablaProsiciones = {}
                    tablaProsiciones['puesto'] = i
                    tablaProsiciones['logo'] = s['team']['logos']
                    tablaProsiciones['name'] = s['team']['name']
                    tablaProsiciones['pj'] = s['stats'][3]
                    tablaProsiciones['g'] = s['stats'][0]
                    tablaProsiciones['e'] = s['stats'][2]
                    tablaProsiciones['p'] = s['stats'][1]
                    tablaProsiciones['gf'] = s['stats'][4]
                    tablaProsiciones['gc'] = s['stats'][5]
                    tablaProsiciones['dif'] = s['stats'][9]
                    tablaProsiciones['pts'] = s['stats'][6]

                    datos.append(tablaProsiciones)

                    i +=1

                    
                return datos
    
    return ''

def tablaLibertadores(params={}):
    response = generate_request('https://site.web.api.espn.com/apis/v2/sports/soccer/conmebol.libertadores/standings?region=ar&lang=es&contentorigin=deportes&sort=rank%3Aasc', params)
                                
    if response:
        
        fixture = response['children']
        i = 1
        datos = list() 
        for t in fixture:
        
            if t['id'] == "3":
                #return  t['standings']['entries']
                for s in t['standings']['entries']:
            
                    tablaProsiciones = {}
                    tablaProsiciones['puesto'] = i
                    tablaProsiciones['logo'] = s['team']['logos']
                    tablaProsiciones['name'] = s['team']['name']
                    tablaProsiciones['pj'] = s['stats'][3]
                    tablaProsiciones['g'] = s['stats'][0]
                    tablaProsiciones['e'] = s['stats'][2]
                    tablaProsiciones['p'] = s['stats'][1]
                    tablaProsiciones['gf'] = s['stats'][4]
                    tablaProsiciones['gc'] = s['stats'][5]
                    tablaProsiciones['dif'] = s['stats'][9]
                    tablaProsiciones['pts'] = s['stats'][6]

                    datos.append(tablaProsiciones)

                    i +=1

                    
                return datos
    
    return ''

def goles(params={}):
    response = generate_request('https://site.web.api.espn.com/apis/site/v2/sports/soccer/ARG.COPA_LPF/teams/21/statistics?region=ar&lang=es&contentorigin=deportes&level=1', params)
    
    if response:
        
        fixture = response['results']['stats']
        i = 1
        datos = list()
        asist = list()
        est = {}

        for t in fixture:
            
            if t['name'] == 'goalsLeaders':
                for s in t['leaders']:
                    

                    tablaProsiciones = {}
                    tablaProsiciones['puesto'] = i
                    tablaProsiciones['name'] = s['athlete']['displayName']
                    tablaProsiciones['pj'] = s['athlete']['statistics'][0]
                    tablaProsiciones['g'] = s['athlete']['statistics'][1]

                    datos.append(tablaProsiciones)
                    i +=1
                    if i == 11:
                        break

                

                est['goles'] = datos
            else:
                i = 1
                for s in t['leaders']:
                    

                    tablaProsiciones = {}
                    tablaProsiciones['puesto'] = i
                    tablaProsiciones['name'] = s['athlete']['displayName']
                    tablaProsiciones['pj'] = s['athlete']['statistics'][0]
                    tablaProsiciones['a'] = s['athlete']['statistics'][2]

                    asist.append(tablaProsiciones)
                    i +=1
                    if i == 11:
                        break
                
                est['asist'] = asist

        return est
         
        
    return ''


def tarjetas(params={}):
    response = generate_request('https://site.web.api.espn.com/apis/site/v2/sports/soccer/ARG.COPA_LPF/teams/21/statistics?region=ar&lang=es&contentorigin=deportes&level=2', params)
    
    if response:
        
        fixture = response['results']['stats']
        i = 1
        datos = list()

        for t in fixture:
            
                

            tablaProsiciones = {}
            tablaProsiciones['puesto'] = i
            tablaProsiciones['name'] = t['displayName']
            tablaProsiciones['pj'] = t['statistics'][0]
            tablaProsiciones['tr'] = t['statistics'][1]
            tablaProsiciones['ta'] = t['statistics'][2]
            datos.append(tablaProsiciones)
            i +=1
            if i == 11:
                break
        
        return datos
         
        
    return ''