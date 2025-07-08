import smtplib, os, hashlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from pathlib import Path
from datetime import datetime

def enviar_email_con_adjunto(
        smtp_server: str,
        smtp_port: int,
        username: str,
        password: str,
        destinatario: str,
        asunto: str,
        cuerpo: str,
        ruta_adjunto: str
):
    try:
        mensaje = MIMEMultipart()
        mensaje["From"] = username
        mensaje["To"] = destinatario
        mensaje["Subject"] = asunto

        mensaje.attach(MIMEText(cuerpo, "plain"))

        ruta = Path(ruta_adjunto)
        if ruta.exists():
            with open(ruta, "rb") as f:
                adjunto = MIMEApplication(f.read(), Name=ruta.name)
            adjunto["Content-Disposition"] = f'attachment; filename="{ruta.name}"'
            mensaje.attach(adjunto)
        else:
            print(f"⚠️ No se encontró el archivo para adjuntar: {ruta_adjunto}")

        with smtplib.SMTP(smtp_server, smtp_port) as servidor:
            servidor.starttls()
            servidor.login(username, password)
            #servidor.send_message(mensaje) #->Descomentar esta linea al tener servidor de correos activo
            print("✅ Correo enviado correctamente.")

    except Exception as e:
        print("❌ Error al enviar el correo:", e)



def calcular_hash(archivo):
    hash_md5 = hashlib.md5()
    with open(archivo, "r", encoding="utf-8") as f:
        lineas  = f.readlines()
        lineas = lineas[:-1]#ignora la ultima linea (fecha)
        contenido = "".join(lineas).encode("utf-8") 
        hash_md5.update(contenido)
    
    return hash_md5.hexdigest()

def eliminar_duplicados_en_reportes():
    carpeta = "reportes"
    archivos = [f for f in os.listdir(carpeta) if f.endswith(".txt")]

    hashes_vistos = {}
    duplicados = []

    for archivo in archivos:
        ruta = os.path.join(carpeta, archivo)
        if not os.path.isfile(ruta):
            continue

        try:
            hash_actual = calcular_hash(ruta)
        except Exception as e:
            print(f"❌ No se pudo calcular hash de {ruta}: {e}")
            continue

        if hash_actual in hashes_vistos:
            duplicados.append(ruta)
        else:
            hashes_vistos[hash_actual] = ruta

    if duplicados:
        for archivo in duplicados:
            os.remove(archivo)
            print(f"🗑️ Eliminado duplicado: {archivo}")
            registrar_log_eliminado(archivo)
    else:
        print("✅ No se encontraron duplicados por contenido.")

def registrar_log_eliminado(nombre_archivo):
    log_path = os.path.join("reportes", "log.txt")
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a", encoding="utf-8") as log:
        log.write(f"[{ahora}] Eliminado duplicado: {nombre_archivo}\n")

def mostrar_menu():
    print("\n📊 MONITOREO CLIMÁTICO - MENÚ PRINCIPAL")
    print("1. Consultar clima y guardar en histórico")
    print("2. Eliminar duplicados del CSV histórico")
    #print("2. Verificar alerta por clima extremo")
    print("3. Graficar temperaturas de una ciudad")
    print("4. Salir")

def mostrar_reporte(clima):
    print("\n=== Clima Actual ===")
    print(f"🌍 Ciudad: {clima['ciudad']}, {clima['pais']}")
    print(f"🌤️  Estado: {clima['descripcion']}")
    print(f"🌡️  Temperatura: {clima['temperatura']} °C")
    print(f"💧 Humedad: {clima['humedad']}%")
    print(f"🌬️ Viento: {clima['viento']} m/s")
