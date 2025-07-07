from clima_api import consultar_clima
from utils.utils_archivos import guardar_reporte, registrar_log
from utils.alertas import detectar_alertas
from utils.utils import enviar_email_con_adjunto

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
        nombre_archivo = guardar_reporte(clima)
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

            enviar_email_con_adjunto(
                smtp_server="ejemplo.com",#cambiar a datos reales del server
                smtp_port=2525,#cambiar a datos reales del server
                username="ejemplo.com",#cambiar a datos reales del server
                password="ejemplo3",#cambiar a datos reales del server
                destinatario="ejemplo.com",
                asunto="Reporte del clima 🌤️",
                cuerpo="Adjunto el reporte automático del clima.",
                ruta_adjunto=nombre_archivo
            )
        else:
            print("✅ Sin alertas.")
            
    else:
        print("⚠️ No se pudo obtener el clima.")

    