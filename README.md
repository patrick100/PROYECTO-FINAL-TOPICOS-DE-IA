# Fingerprint-Classification-System-Through-LENET
Fingerprint classification system using fingerprint orientantion feature vectors of ROI images obtained after passing through different modules of a LENET CNN system - Universidad Nacional de San Agustin (Arequipa - 2018).
#Course
- Topics of Artificial Intelligence
#Authors
- Ruben Edwin Hualla Quispe
- Patrick Lazo Colque
# Data Storage Module
- NIST4 database
# Data Preprocessing Module
- Preprocessing stages:
  * Fingerprint Histogram Equalization
  * Fingerprint Gabor Enhancement
  * Fingerprint Threshold Binarization
  * Fingerprint Thinning
- Final results:
  * NIST4 4000 thinned fingerprint images
# Data Feature Extraction Module
- Two features extracted:
  * Region of Interes extraction through ANN detection algorithm
  * Orientation Map 100 and 400 features extraction algorithm
- Final results:
  * Manually extracted training database for roi block detection.
  * NIST4 4000 roi fingerprint images of 200x200px
  * 2 dat files containing:
        * 4000 NIST4 features vectors of 400 values from roi orientation map.
        * 4000 NIST4 features vectors of 100 values from roi orientation map.
# Data Processing and Results Gathering( Classification and Results  Module )
- Fingerprint classification system:
  * Fingerprint classification 
- Final results:
  * Results from experiments of classification system using a  LENET CNN.
  * Nice classification model of more than 90% accuracy found during experimentation available and ready to be loaded in keras.

the preprocessed fingerprint was the following
# PRE-PROCESSING

![alt text](/huella.png "")



# ARQUITECTURA CNN LENET 5
La arquitecura usada esta basada en cnn lenet 5 con
![alt text](/lenet5.png "Arquitectura lenet 5")


El paper base que se utilizo fue Fingerprint classification using convolutional neural networks and ridge orientation images url:https://ieeexplore.ieee.org/document/8285375/



# COMPUTADORA CARACTERÍSTICAS

La computadora donde se realizaron los experimentos tiene las siguientes características
Core i5 5ta generación memoria RAM 8gb con sistema operativo ubuntu 16.04



# FASE DE ENTRENAMIENTO

El tiempo de entrenamiento aproximado fue de una hora  

![alt text](/entrenamiento.png "Entrenamiento")

Al finalizar el entrenamiento se almacena el modelo entrenado en model.h5


# RESULTADOS OBTENIDOS

Se obtuvo la siguiente grafica de precision.
![alt text](/accu.png "Grafica de precision")

Se obtuvo la siguiente grafica de error.
![alt text](/loss.png "Grafica del error")


# FASE DE PRUEBAS

Para poder reconocer a que clase pertenece la huella ingresada ejecutar procesar_imagenes.py
el script tomara todas la imagenes en la carpeta y las convertira a vectores caracteristica almacenado en test.csv.


![alt text](/vectores.png "Vectores Caracteristica")


Con los vectores caracteristicas ejecutamos el script load.py el cual cargara el modelo de entrenamiento
antes guardado y realizara la prediccion de cada vector caracteristica.


![alt text](/prediccion.png "Prediccion de las Huellas")
