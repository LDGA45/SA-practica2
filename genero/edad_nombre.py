import requests

def obtener_edad_por_nombre(nombre):
    url = f'https://api.agify.io/?name={nombre}'
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        if 'age' in datos:
            return datos['age']
        else:
            return 'Edad desconocida'
    else:
        return 'Error al consultar la API'
