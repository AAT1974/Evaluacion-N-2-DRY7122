import requests

# Valores fijos para Jenkins
ciudad_origen = "Santiago"
ciudad_destino = "Buenos Aires"

def obtener_datos_clima(ciudad):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={ciudad}"
    respuesta = requests.get(url)
    datos = respuesta.json()
    
    if "results" not in datos or not datos["results"]:
        print(f"No se encontró la ciudad: {ciudad}")
        return None

    lat = datos["results"][0]["latitude"]
    lon = datos["results"][0]["longitude"]

    url_clima = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    respuesta_clima = requests.get(url_clima)
    datos_clima = respuesta_clima.json()

    temperatura = datos_clima["current_weather"]["temperature"]
    return temperatura

temp_origen = obtener_datos_clima(ciudad_origen)
temp_destino = obtener_datos_clima(ciudad_destino)

if temp_origen is not None and temp_destino is not None:
    print(f"Temperatura actual en {ciudad_origen}: {temp_origen}°C")
    print(f"Temperatura actual en {ciudad_destino}: {temp_destino}°C")
    diferencia = abs(temp_origen - temp_destino)
    print(f"Diferencia de temperatura: {diferencia}°C")
else:
    print("No se pudo obtener información de ambas ciudades.")

