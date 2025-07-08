import os, csv
import matplotlib.pyplot as plt
from datetime import datetime

def graficar_temperatura(ciudad):
    ruta_csv = os.path.join("data",  f"historico_{ciudad.lower()}.csv")
    print(ruta_csv)

    if not os.path.exists(ruta_csv):
        print("❌ No hay datos históricos para esta ciudad.")
        return
    
    fechas = []
    temperaturas = []

    with open(ruta_csv, newline='', encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                fecha = datetime.strptime(fila['fecha'], "%Y-%m-%d %H:%M:%S")
                temp = float(fila['temperatura'].replace(",", "."))
                fechas.append(fecha)
                temperaturas.append(temp)
            except Exception as e:
                print("⚠️ Error procesando fila:", fila)
                continue
    
    if not fechas:
        print("⚠️ No se encontraron datos válidos para graficar.")
        return
    
    plt.figure(figsize=(10, 5))
    plt.plot(fechas, temperaturas, marker='o')
    plt.title(f"Temperatura en {ciudad.title()}")
    plt.xlabel("Fecha y hora")
    plt.ylabel("Temperatura (°C)")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
