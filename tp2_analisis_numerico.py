import cv2
import numpy as np

def process_image(img):
    # Convertir la imagen de BGR a HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Definir los umbrales para el color amarillo
    umbral_amarillo_inferior = np.array([20, 50, 50])
    umbral_amarillo_superior = np.array([30, 255, 255])

    # Crear la máscara
    mascara = cv2.inRange(hsv, umbral_amarillo_inferior, umbral_amarillo_superior)

    # Aplicar la máscara al canal de saturación
    canal_s = hsv[:,:,1]
    mascara_s = cv2.bitwise_and(canal_s, canal_s, mask=mascara)

    # Usar el algoritmo de Canny para detectar los bordes
    bordes = cv2.Canny(mascara_s, 50, 150)
    
    cv2.imshow('Máscara de Canny', bordes)

    # Crear un elemento estructurante
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

    # Dilatar los bordes
    dilatado = cv2.dilate(bordes, kernel, iterations=1)

    # Aplicar una operación de cierre
    cerrado = cv2.morphologyEx(dilatado, cv2.MORPH_CLOSE, kernel, iterations=1)

    # Encontrar los contornos
    contornos, _ = cv2.findContours(cerrado.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Llenar los contornos
    rellenado = cv2.drawContours(cerrado, contornos, -1, (255,255,255), thickness=cv2.FILLED)

    # Calcular el área de cada contorno
    areas = [cv2.contourArea(cnt) for cnt in contornos]

    # Calcular el área total del color amarillo
    area_total_amarilla = sum(areas)

    # Calcular el área total de la imagen
    area_total_imagen = img.shape[0] * img.shape[1]

    # Calcular el área del color amarillo con respecto al área total de la imagen
    porcentaje_amarillo = (area_total_amarilla / area_total_imagen) * 100

    print(f'El área de color amarillo representa el {porcentaje_amarillo}% del área total de la imagen.')

    # Convertir la imagen cerrada en una máscara binaria
    mascara_cerrada = cerrado > 0

    # Usar la máscara para seleccionar solo los píxeles amarillos en la imagen original
    pixeles_amarillos = img[mascara_cerrada]

    # Sumar todas las intensidades de estos píxeles para obtener la intensidad total del color amarillo
    intensidad_amarilla_total = np.sum(pixeles_amarillos)

    print(f'La intensidad total del color amarillo es {intensidad_amarilla_total}.')

    return rellenado, intensidad_amarilla_total

# Procesar las dos imágenes
img1 = cv2.imread('C:/Users/mpivi/OneDrive/Escritorio/TP2_analisis numerico/im1_tp2.jpg') #carpeta im1
img2 = cv2.imread('C:/Users/mpivi/OneDrive/Escritorio/TP2_analisis numerico/im2_tp2.jpg') #carpeta im2

rellenado1,intensidad1 = process_image(img1)
rellenado2,intensidad2 = process_image(img2)

cv2.imshow('Imagen rellena 1', rellenado1)
cv2.imshow('Imagen rellena 2', rellenado2)

if(intensidad1 > intensidad2):
    print("La primera imagen tiene más cantidad de muestra.")
elif(intensidad1 < intensidad2):
    print("La segunda imagen tiene más cantidad de muestra.")
else: 
    print("Las dos imágenes tienen la misma cantidad de muestra.")

cv2.waitKey(0)
