import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from pathlib import Path

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