import wfdb #libreria para leer senales biologicas
import math #libreria para realizar calculos matematicos
import matplotlib.pyplot as plt #libreria para graficar como en matlab
import numpy as np  # permite crear vectores y matrices multidimencionales


senal_o = wfdb.rdrecord('a08') #lectura de la señal
valores = senal_o.p_signal[:1000,0]
 # porcion de la señal que se va a graficar almacenada en un vector

plt.plot(valores) #grafica
plt.title("Señal original")
plt.xlabel("Frecuencia ")
plt.ylabel("Amplitud")
plt.show() #pestaña de la grafica o figura


#para determinar la desviacion estandar
#forma aplicada
#se obtiene la longitud y la suma del vector 'valores'
longitud = len(valores)
suma = sum(valores)

#una vez obtenidos los datos de longitud y suma se halla la media
media = suma/longitud
print('Valor de la media', media)
 #para d determinar la potencia de la senal
 #creo un  vector de ceros con la longitud del vector valores
 #para almacenar los datos del vector valores elevados al cuadrado
 #en mi nuevo vector con un ciclo for
valores_al_cuadrado =np.zeros(longitud) #creo vector
for i in range(longitud):
   valores_al_cuadrado[i]=valores[i]**2 #almaceno datos

num=np.zeros(longitud)
for j in range(longitud):
    num[j] = (valores[j]-media)**2

suma_num =  sum(num)   

   
desviacion_estandar = math.sqrt(suma_num/(longitud))
print('Desviacion estandar paso a paso',desviacion_estandar)
   
   #para determinar la desviacion estandar
   #utilizando funciones de python

desviacion_std_corta = np.std(valores)
print('funcion std: ',desviacion_std_corta)

#coeficiente de varianza
 
Cv = desviacion_estandar/media
print('El coeficiente de varianza: ',Cv)

#primero normalizamos la 
#normalizacion = (valores-media)/desviacion_estandar
#histograma con funcion
#histogram = plt.hist(normalizacion,bins=10,edgecolor='yellow',desity =True )
#plt.show(2)

#Que la relacion señal ruido?
# es la relacion entre la potencia de la señal y la potencia del ruido
# Generar ruido gaussiano
#crear ruido gaussiano
#crear ruido gaussiano
sumapotencia=sum(valores_al_cuadrado)
potencia = sumapotencia/longitud
numerosazar=np.zeros(longitud)
numeros_aleatorios=numerosazar
for i in range(longitud):
 numeros_aleatorios[i]=np.random.randn()

ruido_gaussiano=(0.9*numeros_aleatorios)/125
plt.plot(ruido_gaussiano)
plt.title("Ruido Gaussiano")
plt.xlabel("Frecuencia ")
plt.ylabel("Amplitud (dB)")
plt.show()

signal_ruidg=valores+ruido_gaussiano
plt.plot(signal_ruidg)
plt.title("Señal contaminada ruido gaussiano")
plt.xlabel("Frecuencia ")
plt.ylabel("Amplitud(dB)")
plt.show()
ruido_gaussiano1=(2*numeros_aleatorios)/125
plt.plot(ruido_gaussiano1)
plt.title("Señal contaminada ruido gaussiano 2")
plt.xlabel("Frecuencia ")
plt.ylabel("Amplitud")
plt.show()

valores_cuadradosg=np.zeros(longitud)
for i in range(longitud):
    valores_cuadradosg[i]=ruido_gaussiano[i]**2
sumag=sum(valores_cuadradosg)
potenciag=sumag/longitud

SNRg=10*np.log10(potencia/potenciag)
print('relacion ruido ',SNRg)

#Ruido artefacto con la señal
Fs=1500
F=10
t=np.arange(0,longitud,1/Fs)
y=(0.7*np.tan(2*np.pi*F*t)[:1000])/125
plt.plot(y[:100])
plt.title("Señal artefacto")
plt.xlabel("Frecuencia ")
plt.ylabel("Amplitud")
plt.show()
signal_ruidoa=valores+y
plt.plot(signal_ruidoa)
plt.title("Señal Ruido artefacto")
plt.xlabel("Frecuencia ")
plt.ylabel("Amplitud")
plt.show()
y2=(2*np.tan(8*np.pi*F*t)[:1000])/125
signal_ruidoa1=valores+y2
plt.plot(signal_ruidoa1)
plt.title("Señal Ruido artefacto 2")
plt.xlabel("Frecuencia ")
plt.ylabel("Amplitud")
plt.show()

valores_cuadradosa=np.zeros(longitud)
for i in range(longitud):
    valores_cuadradosa[i]=y[i]**2
sumaa=sum(valores_cuadradosa)
potenciaa=sumaa/longitud
print('potencia de la señal ruido a: ',potenciaa)
SNRa=10*np.log10(potencia/potenciaa)
print('SNRa ',SNRa)

#ruido impulso
ti=np.arange(0,longitud,1)
impulso=(ti==500)*0.7
signal_impulso=valores+impulso
plt.plot(signal_impulso)
plt.title("ruido impulso")
plt.show()

valores_cuadradosi=np.zeros(longitud)
for i in range(longitud):
    valores_cuadradosi[i]=impulso[i]**2
    
sumai=sum(valores_cuadradosi)
potenciai=sumai/longitud
print('potencia de la señal impulso: ',potenciai)

SNRi=10*np.log10(potencia/potenciai)
print('SNRi ',SNRi)
#histograma
normalizacion=(valores-media)/desviacion_estandar
plt.hist(normalizacion,bins=10,edgecolor='black',density=True)
plt.title("Histograma")
plt.show()