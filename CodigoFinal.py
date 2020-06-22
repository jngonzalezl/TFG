#Lectura experimentación - 14 días - Dos semanas
import statistics
import numpy as np
from os import listdir
import os
import numpy as np
import matplotlib.pyplot as plt

uno = []
dos = []
tres = []
cuatro = []
cinco = []
seis = []
siete = []
ocho = []
nueve = []
diez = []
once = []
doce = []
trece = []
catorce = []

startpoints = []
finpoints = []
totalPoints = []
porcentajes = []

#Lectura de la carpeta donde se encuentran los datos de experimentacion
archivos = []
d = "./Documents/Experimentacion"
for path in os.listdir(d):
    full_path = os.path.join(d, path)
    if os.path.isfile(full_path):
        archivos.append(full_path)

for ar in archivos:
    with open(ar, "r") as ins:
        if "001" in ar:
            for line in ins:
                fields = line.split(";")
                uno.append(fields[1])
        if "002" in ar:
            for line in ins:
                fields = line.split(";")
                dos.append(fields[1])
        if "003" in ar:
            for line in ins:
                fields = line.split(";")
                tres.append(fields[1])
        if "004" in ar:
            for line in ins:
                fields = line.split(";")
                cuatro.append(fields[1])
        if "005" in ar:
            for line in ins:
                fields = line.split(";")
                cinco.append(fields[1])
        if "006" in ar:
                for line in ins:
                    fields = line.split(";")
                    seis.append(fields[1])
        if "007" in ar:
                for line in ins:
                    fields = line.split(";")
                    siete.append(fields[1])               
        if "008" in ar:
            for line in ins:
                fields = line.split(";")
                ocho.append(fields[1])
        if "009" in ar:
            for line in ins:
                fields = line.split(";")
                nueve.append(fields[1])
        if "010" in ar:
            for line in ins:
                fields = line.split(";")
                diez.append(fields[1])
        if "011" in ar:
            for line in ins:
                fields = line.split(";")
                once.append(fields[1])
        if "012" in ar:
            for line in ins:
                fields = line.split(";")
                doce.append(fields[1])
        if "013" in ar:
                for line in ins:
                    fields = line.split(";")
                    trece.append(fields[1])
        if "014" in ar:
                for line in ins:
                    fields = line.split(";")
                    catorce.append(fields[1])   

MediaSizeTotal = round((len(uno) + len(dos) + len(tres) + len(cuatro) + len(cinco) + len(seis) + len(siete) + len(ocho) + len(nueve) + len(diez) + len(once) + len(doce) + len(trece) + len(catorce))/14)
SizeTotal = (len(uno) + len(dos) + len(tres) + len(cuatro) + len(cinco) + len(seis) + len(siete) + len(ocho) + len(nueve) + len(diez) + len(once) + len(doce) + len(trece) + len(catorce))

#Obtencion de informacion importante para la creacion de datos sinteticos

#UNO
punoPorcFin = float(uno[len(uno)-1]) # Para recoger el ultimo porcentaje, porque cuando no esta duplicado es el ultimo porcentaje
for p in range(len(uno)):
    punoF = float(uno[p])
    if (punoF != 0.0) and (len(startpoints)==0):
        startpoints.append(p + 1)
    if (len(startpoints) != 0) and (len(finpoints) == 0):
        porcentajes.append(punoF)
    if punoF == punoPorcFin and len(finpoints) == 0 and len(startpoints) != 0: 
        #Para dejar el primer valor que coincida, por eso es 2
        finpoints.append(p + 2)

totalPoints.append(finpoints[0]-startpoints[0])

#DOS
pdosPorcFin = float(dos[len(dos)-1])
for p in range(len(dos)):
    pdosF = float(dos[p])
    if (pdosF != 0.0) and (len(startpoints)==1):
        startpoints.append(p + 1)
    if (len(startpoints) != 1) and (len(finpoints) == 1):
        porcentajes.append(pdosF)
    if pdosF == pdosPorcFin and len(finpoints) == 1 and len(startpoints) != 1: 
        finpoints.append(p + 2)
    
totalPoints.append(finpoints[1]-startpoints[1])

#TRES
ptresPorcFin = float(tres[len(tres)-1])
for p in range(len(tres)):
    ptresF = float(tres[p])
    if (ptresF != 0.0) and (len(startpoints) == 2):
        startpoints.append(p + 1)
    if (len(startpoints) != 2) and (len(finpoints) == 2):
        porcentajes.append(ptresF)
    if ptresF == ptresPorcFin and len(finpoints) == 2 and len(startpoints) != 1: 
        finpoints.append(p + 2)

totalPoints.append(finpoints[2]-startpoints[2])

#CUATRO
pcuatroPorcFin = float(cuatro[len(cuatro)-1])
for p in range(len(cuatro)):
    pcuatroF = float(cuatro[p])
    if (pcuatroF != 0.0) and (len(startpoints) == 3):
        startpoints.append(p + 1)
    if (len(startpoints) != 3) and (len(finpoints) == 3):
        porcentajes.append(pcuatroF)
    if pcuatroF == pcuatroPorcFin and len(finpoints) == 3 and len(startpoints) != 3: 
        finpoints.append(p + 2)

totalPoints.append(finpoints[3]-startpoints[3])

#CINCO
pcincoPorcFin = float(cinco[len(cinco)-1])
for p in range(len(cinco)):
    pcincoF = float(cinco[p])
    if (pcincoF != 0.0) and (len(startpoints)  == 4):
        startpoints.append(p + 1)
    if (len(startpoints)  != 4) and (len(finpoints)  == 4):
        porcentajes.append(pcincoF)
    if pcincoF == pcincoPorcFin and len(finpoints)  == 4 and len(startpoints)  != 4: 
        finpoints.append(p + 2)

totalPoints.append(finpoints[4]-startpoints[4])

#SEIS
pseisPorcFin = float(seis[len(seis)-1])
for p in range(len(seis)):
    pseisF = float(seis[p])
    if (pseisF != 0.0) and (len(startpoints) == 5):
        startpoints.append(p + 1)
    if (len(startpoints) != 5) and (len(finpoints)  == 5):
        porcentajes.append(pseisF)
    if pseisF == pseisPorcFin and len(finpoints)  == 5 and len(startpoints) != 5: 
        finpoints.append(p + 2)

totalPoints.append(finpoints[5]-startpoints[5])

#SIETE
psietePorcFin = float(siete[len(siete)-1])
for p in range(len(siete)):
    psieteF = float(siete[p])
    if (psieteF != 0.0) and (len(startpoints) == 6):
        startpoints.append(p + 1)
    if (len(startpoints) != 6) and (len(finpoints) == 6):
        porcentajes.append(psieteF)
    if psieteF == psietePorcFin and len(finpoints) == 6 and len(startpoints) != 6: 
        finpoints.append(p + 2)

totalPoints.append(finpoints[6]-startpoints[6])

#OCHO
pochoPorcFin = float(ocho[len(ocho)-1]) 
for p in range(len(ocho)):
    pochoF = float(ocho[p])
    if (pochoF != 0.0) and (len(startpoints)==7):
        startpoints.append(p + 1)
    if (len(startpoints) != 7) and (len(finpoints) == 7):
        porcentajes.append(pochoF)
    if pochoF == pochoPorcFin and len(finpoints) == 7 and len(startpoints) != 7: 
        finpoints.append(p + 2)

totalPoints.append(finpoints[7]-startpoints[7])

#NUEVE
pnuevePorcFin = float(nueve[len(nueve)-1])
for p in range(len(nueve)):
    pnueveF = float(nueve[p])
    if (pnueveF != 0.0) and (len(startpoints)==8):
        startpoints.append(p + 1)
    if (len(startpoints) != 8) and (len(finpoints) == 8):
        porcentajes.append(pnueveF)
    if pnueveF == pnuevePorcFin and len(finpoints) == 8 and len(startpoints) != 8: 
        finpoints.append(p + 2)
    
totalPoints.append(finpoints[8]-startpoints[8])

#DIEZ
pdiezPorcFin = float(diez[len(diez)-1])
for p in range(len(diez)):
    pdiezF = float(diez[p])
    if (pdiezF != 0.0) and (len(startpoints) == 9):
        startpoints.append(p + 1)
    if (len(startpoints) != 9) and (len(finpoints) == 9):
        porcentajes.append(pdiezF)
    if pdiezF == pdiezPorcFin and len(finpoints) == 9 and len(startpoints) != 9: 
        finpoints.append(p + 2)

totalPoints.append(finpoints[9]-startpoints[9])

#ONCE
poncePorcFin = float(once[len(once)-1])
for p in range(len(once)):
    ponceF = float(once[p])
    if (ponceF != 0.0) and (len(startpoints) == 10):
        startpoints.append(p + 1)
    if (len(startpoints) != 10) and (len(finpoints) == 10):
        porcentajes.append(ponceF)
    if ponceF == poncePorcFin and len(finpoints) == 10 and len(startpoints) != 10: 
        finpoints.append(p + 2)

totalPoints.append(finpoints[10]-startpoints[10])

#DOCE
pdocePorcFin = float(doce[len(doce)-1])
for p in range(len(doce)):
    pdoceF = float(doce[p])
    if (pdoceF != 0.0) and (len(startpoints)  == 11):
        startpoints.append(p + 1)
    if (len(startpoints)  != 11) and (len(finpoints)  == 11):
        porcentajes.append(pdoceF)
    if pdoceF == pdocePorcFin and len(finpoints)  == 11 and len(startpoints)  != 11: 
        finpoints.append(p + 2)

totalPoints.append(finpoints[11]-startpoints[11])

#TRECE
ptrecePorcFin = float(trece[len(trece)-1])
for p in range(len(trece)):
    ptreceF = float(trece[p])
    if (ptreceF != 0.0) and (len(startpoints) == 12):
        startpoints.append(p + 1)
    if (len(startpoints) != 12) and (len(finpoints)  == 12):
        porcentajes.append(ptreceF)
    if ptreceF == ptrecePorcFin and len(finpoints)  == 12 and len(startpoints) != 12: 
        finpoints.append(p + 2)

totalPoints.append(finpoints[12]-startpoints[12])

#CATORCE
pcatorcePorcFin = float(catorce[len(catorce)-1])
for p in range(len(catorce)):
    pcatorceF = float(catorce[p])
    if (pcatorceF != 0.0) and (len(startpoints) == 13):
        startpoints.append(p + 1)
    if (len(startpoints) != 13) and (len(finpoints) == 13):
        porcentajes.append(pcatorceF)
    if pcatorceF == pcatorcePorcFin and len(finpoints) == 13 and len(startpoints) != 13: 
        finpoints.append(p + 2)

totalPoints.append(finpoints[13]-startpoints[13])

MediaPuntoComienzo = DesvPuntoComienzo = 0
MediaPuntoFinal = DesvPuntoFinal = 0
MediaPuntosPor = DesvPuntosPor = 0

#Media y desviacion estandar - PUNTO COMIENZO
MediaPuntoComienzo = np.average(startpoints)
MediaPuntoComienzoRound = round(MediaPuntoComienzo)
DesvPuntoComienzo = statistics.stdev(startpoints)

#Media y desviacion estandar - PUNTO FINAL
MediaPuntoFinal = np.average(finpoints)
MediaPuntoFinalRound = round(MediaPuntoFinal)
DesvPuntoFinal = statistics.stdev(finpoints)

#Media y desviacion estandar - PORCENTAJE PRECISION
MediaPuntosPor = np.average(porcentajes)
DesvPuntosPor = statistics.stdev(porcentajes)

#Resultados de los datos recodigos
print("Media tamaño total experimentacion: ", MediaSizeTotal)
print("Tamaño total experimentacion: ", SizeTotal)
print()
print("Media del punto donde aparece el objeto", MediaPuntoComienzoRound )
print("Desv del punto donde aparece el objeto", DesvPuntoComienzo )
print()
print("Media del punto donde desaparece el objeto", MediaPuntoFinalRound )
print("Desv del punto donde desaparece el objeto", DesvPuntoFinal )
print()
print("Media puntos Porcentaje:", MediaPuntosPor)
print("Desviacion puntos Porcentaje:", DesvPuntosPor)
print()

print(".....................................................................................................................................")
#Creacion datos sinteticos - ENTRENAMIENTO
import numpy as np
import matplotlib.pyplot as plt

PtosTestCom = []
PtosTestFin = []

#Creacion - Puntos tiempo de comienzo
muTimeComTrain = MediaPuntoComienzoRound #Media - Calculada de la experimentacion
sigmaTimeComTrain = DesvPuntoComienzo #Desviacion Estandar - Calculada de la experimentacion

numRTimeComTrain = 100

NPointsRTimeComTrain = []
pointsTimeComTrain = np.random.normal(muTimeComTrain, sigmaTimeComTrain, numRTimeComTrain)

for pt in range(len(pointsTimeComTrain)):
    pointRoundComTrain = round(pointsTimeComTrain[pt])
    NPointsRTimeComTrain.append(pointRoundComTrain)

NPointsRTimeSortedComTrain =sorted(NPointsRTimeComTrain)

print("Puntos time COM creados aplicando los filtros", NPointsRTimeSortedComTrain)
print("Tamaño array de puntos time COM con filtros", len(NPointsRTimeComTrain))
print()

#Creacion - Puntos tiempo del final
DataTrainPor = []
DataTrain1 = []
DataTrainWi = []
DataTrainWiTiempo = []
DataTrainWiPunto = []

muTimeFinTrain = MediaPuntoFinalRound #Media - Calculada de la experimentacion
sigmaTimeFinTrain = DesvPuntoFinal #Desviacion Estandar - Calculada de la experimentacion
numRTimeFinTrain =  100

SizeTrains =14 #Dias sintenticos que se quieren crear para el entrenamiento
wi = 0
wiAnt =0 #wi-1
landa = 10 #λ
p = 0

NPointsRTimeFinTrain = []
pointsTimeFinTrain = np.random.normal(muTimeFinTrain, sigmaTimeFinTrain, numRTimeFinTrain)

for pt in range(len(pointsTimeFinTrain)):
    pointRoundFinTrain = round(pointsTimeFinTrain[pt])
    NPointsRTimeFinTrain.append(pointRoundFinTrain)

NPointsRTimeSortedFinTrain =sorted(NPointsRTimeFinTrain)

print("Puntos time FIN creados aplicando los filtros", NPointsRTimeSortedFinTrain)
print("Tamaño array de puntos time FIN con filtros", len(NPointsRTimeFinTrain))

print("Voy a crear", SizeTrains, "ficheros train")
i = 0

#Creacion dias de entrenamiento
while (i != SizeTrains):
    if (NPointsRTimeSortedComTrain[i] < NPointsRTimeSortedFinTrain[i]):
        NumTrain = i+1
        muPorTrain = MediaPuntosPor #Media - Calculada de la experimentacion
        sigmaPorTrain = DesvPuntosPor #Desviacion Estandar - Calculada de la experimentacion

        print("--TRAIN--", NumTrain)
        print("Inicio:", NPointsRTimeSortedComTrain[i])
        print("Fin:", NPointsRTimeSortedFinTrain[i])

        pointsTrain = NPointsRTimeSortedFinTrain[i] - NPointsRTimeSortedComTrain[i]
        pointsTrainI = int(pointsTrain)
        print("Numero de puntos TRAIN:", pointsTrainI)

        numRPorTrain = pointsTrainI
        pointsPorTrain = np.random.normal(muPorTrain, sigmaPorTrain, numRPorTrain)

        for a in range(int(NPointsRTimeSortedComTrain[i])):
            DataTrainPor.append(0)
            DataTrain1.append(0)

        for p in range(len(pointsPorTrain)):
            DataTrainPor.append(pointsPorTrain[p])
            DataTrain1.append(pointsPorTrain[p])

        for p in range(3916 - int(NPointsRTimeSortedFinTrain[i])):
            DataTrainPor.append(0)
            DataTrain1.append(0)
        tiempo =0
        punto =0

        for k in range(len(DataTrain1)):
            wi = (wiAnt * (1-(1/landa))) + (DataTrain1[k]/landa)
            wiAnt = wi
            if wi < 0.0005:
                wi = 0
            DataTrainWi.append(wi)

            punto = punto + 1
            if wi >= 0.5:
                tiempo = tiempo + 1
                DataTrainWiTiempo.append(tiempo)
                DataTrainWiPunto.append(punto)
            else:
                DataTrainWiTiempo.append(0)
                DataTrainWiPunto.append(0)
        
        DataTrain1.clear()
        i = i+1

        print()
    else:
        print("Es menor")


print("Tamaño TOTAL Data Train Porcentajes", len(DataTrainPor))
print("Tamaño TOTAL Data Train WI", len(DataTrainWi))
print("Tamaño TOTAL Data Train WI Tiempo", len(DataTrainWiTiempo))
print("Tamaño TOTAL Data Train WI Puntos", len(DataTrainWiPunto))

#Grafico donde se reprensetan los dias de entrenamiento creados sinteticamente
'''
plt.plot(DataTrainWi)
plt.title('Synthetic Data Training - Detection Breakfast')
#plt.title('Breakfast detection')
plt.axis([0, 54824, 0, 1])
plt.show()
'''

print(".....................................................................................................................................")
#Creacion datos sinteticos - PRUEBAS
import numpy as np
import matplotlib.pyplot as plt

DataTestPor = []
DataTest1 = []
DataTestWi = []
DataTestWiTiempo = []
DataTestWiPunto = []

wi = 0
wiAnt =0 #wi-1
landa = 10 #λ
p = 0

#Creacion - Puntos tiempo
NPointsRTimeComTest = []
pointsTimeComTest =  np.random.randint(747.75, 1495.5, size=10) #6:00h -> 747.75, 12:00h -> 1495.5
                                                          
NPointsRTimeSortedComTest =sorted(pointsTimeComTest)

print("Puntos TEST time COM creados ordenados", NPointsRTimeSortedComTest)
print()

#print("Tamaño array de puntos time FIN con filtros", len(NPointsRTimeSortedFinTest))

SizeTests = (len(NPointsRTimeSortedComTest))
print("Voy a crear", SizeTests/2, "ficheros test")

pointsPorTest = []
#Creacion dias de pruebas
for i in range(int(SizeTests/2)):
    NumTest = i+1
    NPointsRTimeSortedFinTest = NPointsRTimeSortedComTest[int(SizeTests/2)+i] 
    print("--TEST--", NumTest)
    print("Inicio:", NPointsRTimeSortedComTest[i])
    print("Fin:", NPointsRTimeSortedFinTest)

    PtosTestCom.append(NPointsRTimeSortedComTest[i])
    PtosTestFin.append(NPointsRTimeSortedFinTest)

    pointsTest = NPointsRTimeSortedFinTest - NPointsRTimeSortedComTest[i]
    pointsTestI = int(pointsTest)
    print("Numero de puntos TEST:", pointsTestI)

    pointsPorT = np.random.random_sample((20000,))  

    for r in range(len(pointsPorT)):
        #El porcentaje siempre tiene que ser mayor a 0.5
        if (pointsPorT[r] > 0.5) and (len(pointsPorTest) != pointsTestI): 
            #print(pointsPorT[r])
            pointsPorTest.append(pointsPorT[r])

    print(len(pointsPorTest))

    for a in range(int(NPointsRTimeSortedComTest[i])):
        DataTestPor.append(0)
        DataTest1.append(0)

    for p in range(len(pointsPorTest)):
        DataTestPor.append(pointsPorTest[p])
        DataTest1.append(pointsPorTest[p])

    for p in range(3916 - int(NPointsRTimeSortedFinTest)): #3916 por que es el punto final
        DataTestPor.append(0)
        DataTest1.append(0)
    tiempo = 0
    punto = 0
    for k in range(len(DataTest1)):
        wi = (wiAnt * (1-(1/landa))) + (DataTest1[k]/landa) 
        wiAnt = wi
        if wi < 0.0005:
            wi = 0
        DataTestWi.append(wi)

        punto = punto + 1
        if wi >= 0.5:
            tiempo = tiempo + 1
            DataTestWiTiempo.append(tiempo)
            DataTestWiPunto.append(punto)
        else:
            DataTestWiTiempo.append(0)
            DataTestWiPunto.append(0)

    DataTest1.clear()
    pointsPorTest.clear()

    print()

print("Tamaño TOTAL Data TEST Porcentajes", len(DataTestPor)) 
print("Tamaño TOTAL Data TEST WI", len(DataTestWi))
print("Tamaño TOTAL Data TEST WI Tiempo", len(DataTestWiTiempo))
print("Tamaño TOTAL Data TEST WI Punto", len(DataTestWiPunto))
print("Puntos test Com: ", PtosTestCom)
print("Puntos test Fin: ", PtosTestFin)

#Grafico donde se reprensetan los dias de entrenamiento creados sinteticamente
'''
plt.plot(DataTestWi)
plt.title('Synthetic Data Test - Detection Breakfast')
plt.axis([0, 7832, 0, 1])
plt.show()
'''


print(".....................................................................................................................................")
#Creacion del sistema de detección de anomalias
import numpy as np
import rrcf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("--SISTEMA DE ANOMALIAS--")

#Creacion array tridimensional, con el valor de wi, el punto y el tiempo.
DataTestWiTri = np.zeros((len(DataTestWi), 3))
DataTrainWiTri = np.zeros((len(DataTrainWi), 3))

#Para los datos de pruebas
for a in range(len(DataTestWi)):
    DataTestWiTri[a][0] = DataTestWi[a]
    DataTestWiTri[a][1] = DataTestWiPunto[a]
    DataTestWiTri[a][2] = DataTestWiTiempo[a]

#Para los datos de entrenamiento
for a in range(len(DataTrainWi)):
    DataTrainWiTri[a][0] = DataTrainWi[a]
    DataTrainWiTri[a][1] = DataTrainWiPunto[a]
    DataTrainWiTri[a][2] = DataTrainWiTiempo[a]


print("Media Train wi  -- ",np.average(DataTrainWi))
print("Media Train punto -- ",np.average(DataTrainWiPunto))
print("Media Train tiempo  -- ",np.average(DataTrainWiTiempo))
print("Media Test wi  -- ",np.average(DataTestWi))
print("Media Test punto -- ",np.average(DataTestWiPunto))
print("Media Test tiempo  -- ",np.average(DataTestWiTiempo))

print("TRAIN - Tamaño Wi", len(DataTrainWiTri))   
print("TEST - Tamaño Wi", len(DataTestWiTri))

datosUnidos = []

datosUnidos = np.append(DataTrainWi,DataTestWi)
print("Tamaño array datos unidos:", len(datosUnidos))

#Se comprueba de forma manual los dias de pruebas para detectar el numero de anomalias
    #1º Comprobación --> Que el punto de comienzo este entre 1064 y 1274
    #2º Comprobación --> Que el punto de fin este entre 1214 y 1354

totalPtosAnomalia =0
for x in range(len(PtosTestCom)):
    print("-- TEST --", x+1)
    print(" Comienzo test: ", PtosTestCom[x])
    print(" Fin test: ", PtosTestFin[x])

    if (PtosTestCom[x] > 1064) and (PtosTestCom[x] < 1274) and  (PtosTestFin[x] > 1214) and (PtosTestFin[x] < 1354): 
        print("*No es una anomalia")
    else:
        print("*Hay anomalias, analizarlas...")
        if ((PtosTestCom[x] > 1064) and (PtosTestCom[x] < 1274))and  ((PtosTestFin[x] < 1214) or (PtosTestFin[x] > 1354)): 
            print("  Coincide el comienzo pero no el final")
            if (PtosTestFin[x] > 1354):
                ptosConAnomalias = PtosTestFin[x] - 1354
            else:
                ptosConAnomalias = 1214 - PtosTestFin[x]
            print("Numero de puntos con anomalias", ptosConAnomalias)
            totalPtosAnomalia = totalPtosAnomalia + ptosConAnomalias

        elif ((PtosTestCom[x] < 1064) or (PtosTestCom[x] > 1274)) and  ((PtosTestFin[x] > 1214) and (PtosTestFin[x] < 1354)): 
            print("  Coincide el fin pero no el comienzo")
            if (PtosTestCom[x] > 1274):
                ptosConAnomalias = PtosTestCom[x] - 1274
            else:
                ptosConAnomalias = 1064 - PtosTestCom[x]
            print("Numero de puntos con anomalias", ptosConAnomalias)
            totalPtosAnomalia = totalPtosAnomalia + ptosConAnomalias


        else:
            print("  No coincide ni el comienzo ni el final") 
            if (PtosTestCom[x] < 1064) and (PtosTestFin[x] < 1214):
                ptosConAnomalias = (1214 - PtosTestFin[x]) + ( 1064 - PtosTestCom[x])
            elif (PtosTestCom[x] > 1274) and (PtosTestFin[x] > 1354):
                ptosConAnomalias = (PtosTestFin[x] - 1354) + ( PtosTestCom[x] - 1274)
            else:
                ptosConAnomalias = (1064- PtosTestCom[x]) + ( PtosTestFin[x] - 1354)

            print("Numero de puntos con anomalias", ptosConAnomalias)
            totalPtosAnomalia = totalPtosAnomalia + ptosConAnomalias


    #Con lo anterior ya he calculado los puntos que realmente tienen anomalia, ahora tengo que calcular 
    #cuantos detecta el algoritmo que superen de x umbral, para ver el error que tiene
print()
print("Total puntos con anomalias:", totalPtosAnomalia )

#Establecer parametros de arbol
num_trees = 20
shingle_size = 2
tree_size = 15

#Crear un bosque de arboles vacios
forest = []
for _ in range(num_trees):
    tree = rrcf.RCTree()
    forest.append(tree)

#Se usa el generador de "shingle" para crear una ventana movil
pointsTrain = rrcf.shingle(DataTrainWiTri, size=shingle_size)
pointsTest = rrcf.shingle(DataTestWiTri, size=shingle_size)

#Crear un dict para almacenar el puntaje de anomalía de cada punto
avg_codisp = {}
avg_codispTest = {}

#Arbol para los datos de entrenamiento
def train (forest):
    print("TRAIN")
    # Por cada shingle ...
    for index, point in enumerate(pointsTrain):
        #Por cada arbol en el bosque...
        for tree in forest:
            #Inserta el nuevo punto en el árbol
            tree.insert_point(point, index=index)
            #Calcula codisp en el nuevo punto ...
            new_codisp = tree.codisp(index)
            if not index in avg_codisp:
                avg_codisp[index] = 0
            #Y toma el promedio sobre todos los árboles
            avg_codisp[index] += new_codisp / num_trees

    #print("Forest dentro de train",forest)
    

#Arbol para los datos de pruebas
def test (forest):
    print("TEST")
    indexTrain = len(DataTrainWiTri)
    for index2, point2 in enumerate(pointsTest):   
        for tree in forest:
            #Inserta el nuevo punto en el árbol
            tree.insert_point(point2, index=indexTrain)
            #Calcula codisp en el nuevo punto ...
            new_codisp = tree.codisp(indexTrain)
            #Y toma el promedio sobre todos los árboles
            if not indexTrain in avg_codisp:
                avg_codispTest[index2] = 0
                avg_codisp[indexTrain] = 0

            avg_codisp[indexTrain] += new_codisp / num_trees
            avg_codispTest[index2] += new_codisp / num_trees

            #Elimina el nuevo punto del árbol
            tree.forget_point(indexTrain)
            
        indexTrain= indexTrain + 1

train(forest)
test(forest)


print("Tamaño anormaly score total", len(avg_codisp))
print("Tamaño anormaly score test", len(avg_codispTest))

#Calcular el numero de anomalias detectados por el algoritmo, que superen el filtro
ptosAnomalias= []
for h in range(len(avg_codispTest)):
    if(avg_codispTest[h] > 4000):
        ptosAnomalias.append(avg_codispTest[h])

print("Total puntos detectados como anomalias:", len(ptosAnomalias) )
Acierto = (len(ptosAnomalias)/totalPtosAnomalia)*100
print("Acierto: ", Acierto)


#Grafico donde se representan los datos y las anomalias detectadas.
fig, ax1 = plt.subplots(figsize=(10, 5))

color = 'tab:red'
ax1.set_ylabel('Data', color=color, size=14)
ax1.plot(datosUnidos, color=color)
ax1.tick_params(axis='y', labelcolor=color, labelsize=12)
ax1.set_ylim(0,2)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('CoDisp', color=color, size=14)
ax2.plot(pd.Series(avg_codisp).sort_index(), color=color)
ax2.tick_params(axis='y', labelcolor=color, labelsize=12)
ax2.grid('off')
ax2.set_ylim(0, 137060)
plt.title('Data (red) and anomaly score (blue)', size=14)
plt.show()
