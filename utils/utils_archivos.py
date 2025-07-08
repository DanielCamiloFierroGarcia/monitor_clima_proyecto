import os, csv
from datetime import datetime

# Crear carpeta data si no existe
if not os.path.exists("data"):
    os.makedirs("data")

def crear_directorio_si_no_existe(nombre):
    if not os.path.exists(nombre):
        os.makedirs(nombre)

def guardar_reporte(clima, carpeta="reportes"):
    crear_directorio_si_no_existe(carpeta)
    fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_archivo = f"{carpeta}/reporte_{clima['ciudad']}_{fecha}.txt"

    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write("==== REPORTE CLIMÁTICO ====\n")
        f.write(f"Ciudad: {clima['ciudad']}, {clima['pais']}\n")
        f.write(f"Estado: {clima['descripcion']}\n")
        f.write(f"Temperatura: {clima['temperatura']} °C\n")
        f.write(f"Humedad: {clima['humedad']}%\n")
        f.write(f"Viento: {clima['viento']} m/s\n")
        f.write(f"Fecha: {fecha}\n")

    print(f"📄 Reporte guardado en: {nombre_archivo}")
    return nombre_archivo

def registrar_log(ciudad, archivo="reportes/log.txt"):
    crear_directorio_si_no_existe("reportes")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"[{timestamp}] Consulta de clima en: {ciudad}\n"

    with open(archivo, "a", encoding="utf-8") as f:
        f.write(linea)

def guardar_datos_climaticos(ciudad, datos_clima):
    """
    Guarda los datos de clima en un archivo CSV por ciudad.

    ciudad: str - nombre de la ciudad
    datos_clima: dict - debe tener las claves: temperatura, humedad, viento
    """
    nombre_archivo = f"data/historico_{ciudad.lower()}.csv"
    campos = ["fecha", "temperatura", "humedad", "viento"]

    fila = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperatura": datos_clima.get("temperatura"),
        "humedad": datos_clima.get("humedad"),
        "viento": datos_clima.get("viento")
    }

    archivo_existe = os.path.isfile(nombre_archivo)

    with open(nombre_archivo, mode="a", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=campos)
        if not archivo_existe:
            writer.writeheader()
        writer.writerow(fila)