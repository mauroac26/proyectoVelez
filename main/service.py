import requests

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_username(params={}):
    response = generate_request('https://serpapi.com/searches/f2f2618f7a907b4d/622faa3ac47d3c6f6b3416bc.json', params)
    
    if response:

       equipos = response['knowledge_graph']['jugadores']
       
       print(equipos)
       return equipos

    return ''