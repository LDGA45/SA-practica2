import requests

def obtener_genero_por_nombre(nombre):
    url = f'https://api.genderize.io/?name={nombre}'
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        if 'gender' in datos:
            return datos['gender']
        else:
            return 'Género desconocido'
    else:
        return 'Error al consultar la API'

# Ejemplo de uso
nombre_a_verificar = 'Juan'
genero_estimado = obtener_genero_por_nombre(nombre_a_verificar)
print(f'El género estimado para el nombre {nombre_a_verificar} es: {genero_estimado}')
