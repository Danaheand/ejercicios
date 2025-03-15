import smtplib
from email.mime.text import MIMEText

# Configuración del servidor SMTP (ejemplo con Gmail)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_REMITE = "andradedanahepal@gmail.com"
EMAIL_PASSWORD = "SeManejar25"
EMAIL_DESTINO = "andradedanahepal@gmail.com"

# Crear mensaje
mensaje = MIMEText("Este es un mensaje de prueba enviado automáticamente con Python, el día sabado.")
mensaje["Subject"] = "Correo Automático de Prueba"
mensaje["From"] = EMAIL_REMITE
mensaje["To"] = EMAIL_DESTINO

# Enviar correo
with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()  # Cifrar conexión
    server.login(EMAIL_REMITE, EMAIL_PASSWORD)
    server.sendmail(EMAIL_REMITE, EMAIL_DESTINO, mensaje.as_string())

print("Correo enviado correctamente.")
