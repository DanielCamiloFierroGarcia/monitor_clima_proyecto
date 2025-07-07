from datetime import datetime

def detectar_alertas(clima):
    #ciudad = datos_clima.get("name")
    #clima = datos_clima["main"]
    #temperatura = clima["temp"]
    #humedad = clima["humidity"]

    alertas = []

    if clima["temperatura"] > 30:
        alertas.append("Temperatura extremadamente alta 🥵")
    elif clima["temperatura"] < 0:
        alertas.append("Temperatura bajo cero 🥶")
    if clima["humedad"] > 80:
        alertas.append("Humedad muy alta 💧")
    if clima["viento"] > 40:
        alertas.append("Vientos fuertes 🌪️")


    return alertas