import pandas as pd

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import (SimpleDocTemplate, Paragraph, PageBreak)
#confirmados
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
df = pd.read_csv(url)
start_date = "1/31/20"
clasificador = df[df['Country/Region'] == "Italy"]
confirmados = clasificador.iloc[0].loc[start_date:]
nconfirmados = str(confirmados.at[confirmados.index[-1]])

#muertos
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
df = pd.read_csv(url)
start_date = "1/31/20"
clasificador = df[df['Country/Region'] == "Italy"]
confirmados = clasificador.iloc[0].loc[start_date:]
nfallecidos = str(confirmados.at[confirmados.index[-1]])

#recuperados
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
df = pd.read_csv(url)
start_date = "1/31/20"
clasificador = df[df['Country/Region'] == "Italy"]
confirmados = clasificador.iloc[0].loc[start_date:]
nrecuperados = str(confirmados.at[confirmados.index[-1]])



from datetime import datetime
directorio = "imgs_interciclo/"
w, h = A4
c = canvas.Canvas("reports/reporteinter.pdf", pagesize=A4)


text = c.beginText(170,h - 25)
text.setFont('Times-Bold',17)
text.textLines('Proyecto Final Simulacion RPA')
c.drawText(text)

text = c.beginText(80,h - 60)
text.setFont('Times-Roman',12)
text.textLines('Hernan Leon, Oscar Pizarro, Byron Calva')
c.drawText(text)

text = c.beginText(15,h - 60)
text.setFont('Times-Bold',12)
text.textLines('Integrantes: ')
c.drawText(text)

text = c.beginText(15,h - 80)
text.setFont('Times-Bold',12)
text.textLines('Fecha: ')
c.drawText(text)


text = c.beginText(55,h - 80)
text.setFont('Times-Roman',12)
text.textLines(str(datetime.now()))
c.drawText(text)


t_images= 205
t_imagesw= 500
resta = 40

text = c.beginText(230,h - 130)
text.setFont('Times-Bold',15)
text.textLines('Reporte de Resultados')
c.drawText(text)
#draw logo
c.drawImage(r"C:\Users\opizarro\Documents\ProyectoFinalSimulacion\imgs_interciclo\logo.png", 420,770, width=150, height=50)


###Titulo Grafica Acuracy losss de los modelos
cadena = "Procesos del proyecto interciclo"
text = c.beginText(180, h-160)
text.setFont("Helvetica-Bold", 14)
text.textLines(cadena)
c.drawText(text)
##Accurracy modelo 1 (hacer mas grande la imagen)
cadena = "1) Visualizacion de datos"
text = c.beginText(90, h-190)
text.setFont("Helvetica-Bold", 12)
text.textLines(cadena)
c.drawText(text)

c.drawImage(directorio+"1.png", 50,400+resta, width=t_imagesw, height=t_images)


##Accurracy modelo 2(hacer mas grande la imagen)
cadena = "2) Modelo polinomial"
text = c.beginText(90, h-450)
text.setFont("Helvetica-Bold", 12)
text.textLines(cadena)
c.drawText(text)
c.drawImage(directorio+"2.png", 50,140+resta, width=t_imagesw, height=t_images)


c.showPage()#termina la primera pagina


t_images= 200
t_imagesw= 500
resta = 40

#draw logo
#draw logo
c.drawImage(r"C:\Users\opizarro\Documents\ProyectoFinalSimulacion\imgs_interciclo\logosis.png", 250,680, width=400, height=200)
c.drawImage(r"C:\Users\opizarro\Documents\ProyectoFinalSimulacion\imgs_interciclo\logo.png", 50,730, width=230, height=80)

###Titulo Grafica Acuracy losss de los modelos
cadena = "Procesos del proyecto interciclo"
text = c.beginText(180, h-160)
text.setFont("Helvetica-Bold", 14)
text.textLines(cadena)
c.drawText(text)
##Accurracy modelo 1 (hacer mas grande la imagen)
cadena = "3) Modelo probabilistico"
text = c.beginText(90, h-190)
text.setFont("Helvetica-Bold", 12)
text.textLines(cadena)
c.drawText(text)
c.drawImage(directorio+"3.png", 50,400+resta, width=t_imagesw, height=t_images)


##Accurracy modelo 2(hacer mas grande la imagen)
cadena = "4) Modelo SIR"
text = c.beginText(90, h-450)
text.setFont("Helvetica-Bold", 12)
text.textLines(cadena)
c.drawText(text)
c.drawImage(directorio+"4.png", 50,140+resta, width=t_imagesw, height=t_images)



c.showPage()

c.drawImage(r"C:\Users\opizarro\Documents\ProyectoFinalSimulacion\imgs_interciclo\logosis.png", 250,680, width=400, height=200)
c.drawImage(r"C:\Users\opizarro\Documents\ProyectoFinalSimulacion\imgs_interciclo\logo.png", 50,730, width=230, height=80)


t_images= 200
t_imagesw= 500
resta = 40


###Titulo Grafica Acuracy losss de los modelos
cadena = "Procesos del proyecto interciclo"
text = c.beginText(180, h-160)
text.setFont("Helvetica-Bold", 14)
text.textLines(cadena)
c.drawText(text)
##Accurracy modelo 1 (hacer mas grande la imagen)
cadena = "5) Herramienta Hospital"
text = c.beginText(90, h-190)
text.setFont("Helvetica-Bold", 12)
text.textLines(cadena)
c.drawText(text)
c.drawImage(directorio+"5.png", 50,400+resta, width=t_imagesw, height=t_images)


##Accurracy modelo 2(hacer mas grande la imagen)
cadena = "6) Pagina WEB"
text = c.beginText(90, h-450)
text.setFont("Helvetica-Bold", 12)
text.textLines(cadena)
c.drawText(text)
c.drawImage(directorio+"6.png", 50,140+resta, width=t_imagesw, height=t_images)

c.showPage()


####################################
c.drawImage(r"C:\Users\opizarro\Documents\ProyectoFinalSimulacion\imgs_interciclo\logosis.png", 250,680, width=400, height=200)
c.drawImage(r"C:\Users\opizarro\Documents\ProyectoFinalSimulacion\imgs_interciclo\logo.png", 50,730, width=230, height=80)

#################Conclusiones y Bibliogrrafia

ahora = str(datetime.now()).split(" ")
###Titulo Grafica Acuracy losss de los modelos
cadena = "CONCLUSIONES"
text = c.beginText(220, h-160)
text.setFont("Helvetica-Bold", 17)
text.textLines(cadena)
c.drawText(text)
##Accurracy modelo 1 (hacer mas grande la imagen)
cadena = "- Hoy "+ahora[0]+" siendo las "+ahora[1]+" en Italia se tienen "+\
nconfirmados+" personas \ninfectadas, "+nfallecidos+" personas fallecidas y "+nrecuperados\
+" personas recuperadas debido \na la pandemia del Covid-19, segun los datos tomados de [1].\n\n"\
+"- Se puede ver que la implementacion de RPA a un proceso nos facilita y nos \nahorra tiempo "+\
"permitiendonos realizar otras actividades que normalmente no \nse pueden realizar por falta de tiempo."
text = c.beginText(70, h-190)
text.setFont("Helvetica", 12)
text.textLines(cadena)
c.drawText(text)



##Accurracy modelo 2(hacer mas grande la imagen)
cadena = "REFERENCIAS"
text = c.beginText(220, h-340)
text.setFont("Helvetica-Bold", 17)
text.textLines(cadena)
c.drawText(text)

cadena = "[1] https://github.com/CSSEGISandData/COVID-19.\n\n"+\
"[2] https://www.auraportal.com/es/rpa-robotic-process-automation-que-es/"
text = c.beginText(90, h-380)
text.setFont("Helvetica", 12)
text.textLines(cadena)
c.drawText(text)


c.showPage()



c.save()