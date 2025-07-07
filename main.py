from clima_api import consultar_clima

def mostrar_reporte(clima):
    print("\n=== Clima Actual ===")
    print(f"🌍 Ciudad: {clima['ciudad']}, {clima['pais']}")
    print(f"🌤️  Estado: {clima['descripcion']}")
    print(f"🌡️  Temperatura: {clima['temperatura']} °C")
    print(f"💧 Humedad: {clima['humedad']}%")
    print(f"🌬️ Viento: {clima['viento']} m/s")

if __name__ == "__main__":
    ciudad = input("📍 Ingresa el nombre de la ciudad: ").strip()
    clima = consultar_clima(ciudad)
    if clima:
        mostrar_reporte(clima)
    else:
        print("⚠️ No se pudo obtener el clima.")