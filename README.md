### Laboratorio 2

### Introducción al Código

En este laboratorio, se busca analizar y procesar señales de audio capturadas por tres micrófonos en una sala. El objetivo principal es registrar las señales de ruido de la sala, calcular la relación señal-ruido (SNR) de cada señal y realizar un análisis temporal y espectral de las mismas. Además, se investigarán métodos de separación de fuentes para aislar la señal de interés.

#### Pasos del Proyecto:

**Registro y Adquisición de Señales**:

   Las señales de los micrófonos deben ser registradas y guardadas para su posterior análisis.
   Se grabará el ruido de la sala utilizando tres micrófonos y se calculará el SNR de cada señal. Si alguna señal tiene un SNR insuficiente, se repetirá la medición y se argumentarán las razones.

**Procesamiento de Señales**:

   Se realizará un análisis temporal y espectral de las señales capturadas por cada micrófono. Para el análisis espectral, se utilizará la Transformada de Fourier Discreta (DFT) o la Transformada Rápida de Fourier (FFT), describiendo la información obtenida con cada una.
   Se investigarán métodos de separación de fuentes, como el Análisis de Componentes Independientes (ICA) y el Beamforming, para aislar la señal de interés a partir de las señales capturadas por los micrófonos.

### Descripción del Código

El código proporcionado realiza las siguientes tareas:

1. **Importación de Librerías**:

- Se importan las librerías necesarias para el procesamiento de audio (`librosa`), visualización (`matplotlib`), cálculos numéricos (`numpy`), y análisis de componentes independientes (`FastICA` de `scikit-learn`).

	

		import librosa
		import matplotlib.pyplot as plt
		import numpy as np
		from sklearn.decomposition import FastICA
		import soundfile as sf

2. **Carga de Archivos de Audio**:
    Se cargan tres archivos de audio utilizando `librosa.load`, obteniendo las señales y sus frecuencias de muestreo.
		senal_1, fs_1 = librosa.load('Sonido 1.m4a', sr=None)
		senal_2, fs_2 = librosa.load('Sonido 2.m4a', sr=None)
		senal_3, fs_3 = librosa.load('Sonido 3.m4a', sr=None)
		print('Frecuencia de muestreo del audio 1:', fs_1)
		print('Frecuencia de muestreo del audio 2:', fs_2)
print('Frecuencia de muestreo del audio 3:', fs_3)

3. **Creación de Vectores de Tiempo**:
    Se crean vectores de tiempo para cada señal de audio, necesarios para graficar las señales en función del tiempo.
		tiempo_audio_1 = np.linspace(0, len(senal_1) / fs_1, len(senal_1))
		tiempo_audio_2 = np.linspace(0, len(senal_2) / fs_2, len(senal_2))
		tiempo_audio_3 = np.linspace(0, len(senal_3) / fs_3, len(senal_3))


4. **Configuración de Cuantificación**:
    Se define la resolución de cuantificación en bits y se calculan los niveles de cuantificación.
	 Calcular SNR, Dstd y Potencia
#### Configuración de cuantificación
		bits_audio = 16
		niveles_audio = 2 ** bits_audio

5. **Cálculo de SNR, Potencia y Desviación Estándar**:
     Se definen funciones para calcular la relación señal-ruido (SNR), la potencia de la señal y la desviación estándar.
     Se generan señales de ruido blanco y se calculan los valores de SNR, potencia y desviación estándar para cada señal de audio.

			print('Niveles de cuantificación:', niveles_audio)
		def calcular_snr(signal, noise):
			potencia_senal = np.mean(signal ** 2)
			potencia_ruido = np.mean(noise ** 2)
			snr = 10 * np.log10(potencia_senal / potencia_ruido)
			return snr

		def calcular_potencia(signal):
			return np.mean(signal ** 2)

		def calcular_dstd(signal):
			return np.std(signal)

6. **Impresión de Resultados**:
    Se imprimen los valores calculados de SNR, potencia y desviación estándar.

			snr_1 = calcular_snr(senal_1, ruido)
			snr_2 = calcular_snr(senal_2, ruido)
			snr_3 = calcular_snr(senal_3, ruido)

			potencia_1 = calcular_potencia(senal_1)
			potencia_2 = calcular_potencia(senal_2)
			potencia_3 = calcular_potencia(senal_3)

			dstd_1 = calcular_dstd(senal_1)
			dstd_2 = calcular_dstd(senal_2)
			dstd_3 = calcular_dstd(senal_3)
7. **Graficar Señales de Audio**:
    Se grafican las señales de audio en función del tiempo utilizando `matplotlib`.
  
  				#Audio 1
			plt.plot(tiempo_audio_1, senal_1)
			plt.title('Audio 1')
			plt.xlabel('Tiempo (s)')
			plt.ylabel('Amplitud')
			plt.show()

			# Audio 2
			plt.plot(tiempo_audio_2, senal_2)
			plt.title('Audio 2')
			plt.xlabel('Tiempo (s)')
			plt.ylabel('Amplitud')
			plt.show()

			# Audio 3
			plt.plot(tiempo_audio_3, senal_3)
			plt.title('Audio 3')
			plt.xlabel('Tiempo (s)')
			plt.ylabel('Amplitud')
			plt.show()

###Archivos de Interes

En este laboratorio, los archivos de interés son las grabaciones de audio capturadas por tres micrófonos en una sala. Estos archivos contienen las señales de ruido ambiental que se utilizarán para el análisis y procesamiento.

https://drive.google.com/drive/folders/1DHaIsrKwmep2bYpDj4DohjwdRHiUpmHT


# senales1.1
