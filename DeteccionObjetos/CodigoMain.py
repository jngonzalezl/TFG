#PARA LA EXPERIMENTACIÓN UNICAMENTE CON DESAYUNO
import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile
 
from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image
import time

import psutil

import cv2
import time

#Definir el video stream
cap = cv2.VideoCapture(0)
sys.path.append("..")

from utils import label_map_util
 
from utils import visualization_utils as vis_util
from random import seed

MODEL_FILE = '/Users/jennygonzalez/Documents/models/research/object_detection/IG.tar.gz'
#DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'
 
#Ruta al gráfico de detección de congelados. Este es el modelo real que se utiliza para la detección de objetos.
PATH_TO_CKPT ='IG/frozen_inference_graph.pb'
 
#Lista de las cadenas que se utilizan para agregar la etiqueta correcta para cada cuadro
#PATH_TO_LABELS = '/Users/jennygonzalez/Documents/models/research/object_detection/data/mscoco_label_map.pbtxt'
PATH_TO_LABELS = '/Users/jennygonzalez/Documents/models/research/object_detection/data/label.pbtxt'


#Número de clases a detectar.
NUM_CLASSES = 1

tar_file = tarfile.open(MODEL_FILE)
for file in tar_file.getmembers():
  file_name = os.path.basename(file.name)
  if 'frozen_inference_graph.pb' in file_name:
    tar_file.extract(file, os.getcwd())
    
#Cargue un modelo de Tensorflow (congelado) en la memoria.
detection_graph = tf.Graph()
with detection_graph.as_default():
  od_graph_def = tf.GraphDef()
  with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
    serialized_graph = fid.read()
    od_graph_def.ParseFromString(serialized_graph)
    tf.import_graph_def(od_graph_def, name='')
    
    
#Cargando mapa de etiquetas
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

plt.rcParams['animation.html'] = 'jshtml'

fig = plt.figure(figsize=(10, 6), dpi= 80)
fig.suptitle('Gráficos de las relaciones encontradas', fontsize=16)
ax1=plt.subplot(111)

#ax1 = fig.add_subplot(220)


fig.show()


#FUNCION PARA CALCULAR OBJETOS
def calcularObjetos(todos, wi):
    flag = ""
    #uno = [objetos[x], porcentajes[x], xmin , ymax, xmax ,ymin ]

    print("Funcion para calcular la de un objeto individual")
    print("heyyy")
    for p in range(len(todos)):
        print("Estoy dentro del array")
        print(todos[p])
        print('Porcentaje', todos[p][1])
        lamda = 10
      
        #breakfast
        if (todos[p][0] == "breakfast"):
            print("El objeto que hay en el frame es desayuno")

            #Sino esta vacio el array lo recorro
            #p sera el porcentaje del objeto
            print("Leyendo el array objeto sofa.")
            objeto_Bre[0] = todos[p][0] #nombre
            objeto_Bre[1] = todos[p][1] #porcentaje
            float(objeto_Bre[2])
            print('Este es valor wi del array', objeto_Bre[2])  
            print("Porcentaje es:", todos[p][1])   
            wi = objeto_Bre[2]*(1-1/lamda)+todos[p][1]/lamda
            print('wi:', wi)
            objeto_Bre[2] = wi


                

objeto_Bre = ["breakfast",0,0] #Objeto Desayuno

dirFichero = '/Users/jennygonzalez/Documents/models/research/object_detection/Breakfast.txt'
#Si quiero que se dejen estaticos los objetos que han ido apareciendo
#objetosHay = []

# DETECCION
with detection_graph.as_default():
  with tf.Session(graph=detection_graph) as sess:

    v = 0
    wi = 0
    puntosX, puntosY = [], []
    puntosXP, puntosYP = [], []

    #Para la grafica, las x
    contador =0

    wiB=0 #Breakfast
    tiempoAcumulado = 0.00

    while True:
        #Tiempo
        print("_________________") 
        timeCaptura=  time.strftime("%c")
        print (time.strftime("%c"))

        seconds1 = time.time()
        # Leer frame de la cámara
        ret, image_np = cap.read()
        #Expandir dimensiones ya que el modelo espera que las imágenes tengan forma: [1, None, None, 3]
        image_np_expanded = np.expand_dims(image_np, axis=0)
        # Extraer tensor de imagen.
        image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
        # Extraer cajas de detección
        boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
        #Extraer Scores
        #Cada score representa cómo nivel de confianza para cada uno de los objetos.
        #El score se muestra en la imagen del resultado, junto con la etiqueta de la clase.
        scores = detection_graph.get_tensor_by_name('detection_scores:0')
        # Extraer clases de detección
        classes = detection_graph.get_tensor_by_name('detection_classes:0')
        # Extraer numero de detecciones
        num_detections = detection_graph.get_tensor_by_name('num_detections:0')
        #Detección actual
        (boxes, scores, classes, num_detections) = sess.run(
          [boxes, scores, classes, num_detections],
          feed_dict={image_tensor: image_np_expanded})
        #Visualización de los resultados de una detección.
        vis_util.visualize_boxes_and_labels_on_image_array(
            image_np,
            np.squeeze(boxes),
            np.squeeze(classes).astype(np.int32),
            np.squeeze(scores),
            category_index,
            use_normalized_coordinates=True,
            line_thickness=8)
        
        #Si cada vez que lea el frame se resetee los objetos que hay y solo escriba los que estan en ese momento en el frame
        objetosHay = [] 
        
        final_score = np.squeeze(scores) 
        
        #Porcentajes de cada objetos
        porcentajes = []
        #Nombre de los objetos
        objetos = []

        #Todos los objetos de la pantalla (Nombre, porcentaje, puntos...)
        todos = []
        
        #Mostrar salida
        cv2.imshow('object detection', cv2.resize(image_np, (500,500)))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        count = 0
        
        for i in range(100):
            if scores is None or final_score[i] > 0.1:
                porcentajes.append(final_score[i])
                count = count + 1
                position = boxes[0][0]
                (xmin, xmax, ymin, ymax) = (position[1]*500, position[3]*500, position[0]*500, position[2]*500)
                
        #Cuantos objectos hay en ese momento en la pantalla                
        print('Numero de objetos en pantalla:',count)
        printcount = 0;
        todos = []

        for i in classes[0]:
            printcount = printcount +1
            objetos.append(category_index[i]['name'])
            
            if(printcount == count):
                break
        
        box = np.squeeze(boxes)

        for x in range(count):
            print(objetos[x])
            #print(porcentajes[x])
            ymin = (int(box[x,0]*500))
            xmin = (int(box[x,1]*500))
            ymax = (int(box[x,2]*500))
            xmax = (int(box[x,3]*500))
            print('Punto 1: (',xmin,',',ymax,')')
            #print('Punto 2: (',xmax,',',ymax,')')
            #print('Punto 3: (',xmin,',',ymin,')')
            print('Punto 4: (',xmax,',',ymin,')')
            
            #Solo me hacen falta los puntos 1 y 4
            uno = [objetos[x], porcentajes[x], xmin , ymax, xmax ,ymin ]
            
            todos.append(uno)
        seconds2 = time.time()
        v= v+1
        contador = contador +1
        diferenciaSec = seconds2 - seconds1
        print("Segundos:", diferenciaSec)
        tiempoAcumulado = tiempoAcumulado + diferenciaSec

        calcularObjetos(todos,wi)
        # v = 10 -> Se calcula cada 2 segundos
        if ((tiempoAcumulado) >= 0.91):
            print("Ha entradoooo")
            print("Tiempo Acumulado", tiempoAcumulado)

            tiempoAcumulado = 0
        #if v == 5:
            #print("hey")
                    
            print('ARRAYY Breakast---')
            print(*objeto_Bre)
            
            ##OBJETOSSSSS
            #Desayuno
  
            if (wiB == objeto_Bre[2]):
                print("Se ha mantenido el valor wi, por lo que olvida")
                wiB = wiB * (1-1/10)
                objeto_Bre[2] = wiB
                
                print("1)Pinto el grafico objeto breakfast")

                puntosX.append(contador)
                print('  Valor x:', contador)
                puntosY.append(wiB)
                print('  Valor y:', wiB)

                ax1.plot(puntosX, puntosY, color='b')
                ax1.set_title('Breakfast')

                ax1.set_xlim(left=max(0, contador-30), right=contador+50)

                ##time.sleep(0.3)
                fig.canvas.draw()
            else:
                wiB = objeto_Bre[2]
                
                print("2)Pinto el grafico objeto breakfast")

                puntosX.append(contador)
                print('  Valor x:', contador)
                puntosY.append(wiB)
                print('  Valor y:', wiB)

                ax1.plot(puntosX, puntosY, color='b')
                ax1.set_title('Breakfast')


                ax1.set_xlim(left=max(0, contador-30), right=contador+50)

                ##time.sleep(0.3)
                fig.canvas.draw()

            ###ESCRIBIR EN FICHERO
            fichero = open(dirFichero, 'a')

            #fecha
            fichero.write(timeCaptura + " | ")

            #objetos son los q hay en ese momento
            fichero.write("Objetos: ")

            #Objetos son las generadas en cuanto empieza la ejecucion
            for k in range(len(objeto_Bre)):
                print("Cosas a escribir para el fichero (B)...")
                print(str(objeto_Bre[k]))
                fichero.write(str(objeto_Bre[k])  + ";")
            
            fichero.write("\n")
            fichero.close()
            
            
            v =0

print("YAAA")

