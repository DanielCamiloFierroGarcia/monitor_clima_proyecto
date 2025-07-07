import requests

API_KEY = "b42debb5b5ca260c76409a90f4880898"
URL = "https://api.openweathermap.org/data/2.5/weather"

def consultar_clima(ciudad):
    params = {
        "q": ciudad,
        "appid": API_KEY,
        "units": "metric",
        "lang": "es"
    }

    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()
        datos = response.json()

        clima = {
            "ciudad": datos["name"],
            "pais": datos["sys"]["country"],
            "descripcion": datos["weather"][0]["description"].capitalize(),
            "temperatura": datos["main"]["temp"],
            "humedad": datos["main"]["humidity"],
            "viento": datos["wind"]["speed"]
        }
        return clima
    
    except requests.exceptions.HTTPError as e:
        print("❌ Error al obtener datos del clima:", e)
        return None