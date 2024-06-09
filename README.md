# Trabajo practico 2 de analisis numerico UTN

### Detector colorimetrico
Recientemente, investigadores encontraron una forma de detectar una sustancia de interes a traves de un
metodo colorimetrico, haciendo uso de una tira de papel. El principio de deteccion basico es el cambio de color
debido a la presencia de dicha sustancia. El compuesto utilizado como detector es de color azul originalmente,
y en presencia de la muestra, se torna de color amarillo. A traves de un ensayo de electroforesis, se puede
determinar la evolucion temporal del dispositivo tomando fotos en diferentes instantes de tiempo. A modo de
resumen del experimento, se puede crear un gr´afico con ejes posicion vs tiempo, y un color determinado para
la intensidad de los complejos colorim´etricos. Se adjunta un video de la secuencia de uno de los experimentos
y las fotos que resumen 2 experimentos, con diferentes concentraciones de muestra.

- Convierta las imagenes al espacio de color HSV. Determine umbrales, minimos y maximos, en el canal
de matiz (H) para el color amarillo y cree una mascara.
- Aplique dicha mascara al canal de saturacion (S), y utilice una matriz de convolucion conveniente para
detectar los bordes de la imagen resultante.
- Cree un elemento estructurante sobre los bordes encontrados, dilatelos y aplique una operacion de cierre
para peque˜nos espacios que conecten dichos bordes de manera de obtener un ´area cerrada con frontera
unica y conexa, delimitando en la figura el color amarillo.
- Llene esta ultima area (mascara) y determine el area del color amarillo respecto al area total de la
imagen. Realice las correcciones manuales que considere necesarias observando la imagen inicial.
- Integre la intensidad de amarillo en el area encontrada, y determine qu´e imagen tenia mas cantidad de
muestra y obtenga conclusiones.

