from flask import Flask, request, jsonify
from .edad.genero_nombre import obtener_edad_por_nombre
from .genero.edad_nombre import obtener_genero_por_nombre

app = Flask(__name__)

@app.route('/analizar_nombre', methods=['POST'])
def analizar_nombre():
    datos = request.get_json()

    if 'nombre' in datos:
        nombre = datos['nombre']
        edad_estimada = obtener_edad_por_nombre(nombre)
        genero_estimado = obtener_genero_por_nombre(nombre)

        resultado = {
            'nombre': nombre,
            'edad_estimada': edad_estimada,
            'genero_estimado': genero_estimado
        }

        return jsonify(resultado)
    else:
        return jsonify({'error': 'Parámetro "nombre" no proporcionado'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)