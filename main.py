import time
from clima_api import consultar_clima
from utils.utils_archivos import guardar_reporte, registrar_log, guardar_datos_climaticos
from utils.alertas import detectar_alertas
from utils.utils import enviar_email_con_adjunto, mostrar_menu, mostrar_reporte, eliminar_duplicados_en_reportes
from utils.graficar_ciudad import graficar_temperatura

def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            ciudad = input("📍 Ingresa el nombre de la ciudad: ").strip()
            clima = consultar_clima(ciudad)

            if clima:
                mostrar_reporte(clima)
                nombre_archivo = guardar_reporte(clima)
                registrar_log(ciudad)
                guardar_datos_climaticos(ciudad, clima)

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
                        smtp_server="mail.smtp2go.com",#cambiar a datos reales del server
                        smtp_port=2525,#cambiar a datos reales del server
                        username="popiwor597@datingso.com",#cambiar a datos reales del server
                        password="JY2GqWziOao83bC3",#cambiar a datos reales del server
                        destinatario="dfierro192@gmail.com",
                        asunto="Reporte del clima 🌤️",
                        cuerpo="Adjunto el reporte automático del clima.",
                        ruta_adjunto=nombre_archivo
                    )
                else:
                    print("✅ Sin alertas.")
                    
            else:
                print("⚠️ No se pudo obtener el clima.")
        elif opcion == "2":
            eliminar_duplicados_en_reportes()
        elif opcion == "3":
            ciudad = input("📍 Ingresa el nombre de la ciudad: ").strip()
            graficar_temperatura(ciudad)
        elif opcion == "4":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida. Intenta de nuevo.")
        
        time.sleep(1)

if __name__ == "__main__":
    ejecutar()
    

    