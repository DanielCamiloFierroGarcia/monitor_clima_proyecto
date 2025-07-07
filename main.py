from clima_api import consultar_clima
from utils.utils_archivos import guardar_reporte, registrar_log
from utils.alertas import detectar_alertas

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
        guardar_reporte(clima)
        registrar_log(ciudad)

        alertas = detectar_alertas(clima)

        if alertas:
            print("\n🚨 ALERTAS:")
            for alerta in alertas:
                print(alerta)

            #Guardar tambien en log
            with open("logs/registro.txt", "a", encoding="utf-8") as log:
                for alerta in alertas:
                    log.write(f"[ALERTA] {alerta}\n")
        else:
            print("✅ Sin alertas.")
            
    else:
        print("⚠️ No se pudo obtener el clima.")