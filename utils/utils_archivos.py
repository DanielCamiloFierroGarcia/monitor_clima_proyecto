import os
from datetime import datetime

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