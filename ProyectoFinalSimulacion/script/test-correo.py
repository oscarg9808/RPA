from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import time
destinatarios = ["hleonl@est.ups.edu.ec","cuartoscayambe@gmail.com","jbenavidesc1@est.ups.edu.ec","oscarg9808@hotmail.com"]
for destinatario in destinatarios: 
    subject = "Reporte Covid-19 (3 provincias) son pruebas"
    msg= MIMEMultipart()
    password = "Ec123abcd"
    msg['From'] = "oscarg9808@gmail.com"
    msg['To'] = destinatario
    msg['Subject'] = subject 
      
    cuerpo = "Este es un Flyer generado para la materia de Simulacion \nAutores: Byron Calva, Hernan Leon, Oscar Pizarro\n Son solo pruebas Juan, no estaras bravo chucha :V"
    msg.attach(MIMEText(cuerpo,'plain'))
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.ehlo()
    server.login(msg['From'], password) 
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit() 
    print ("Mensaje enviado: %s:" % (msg['To']))
    