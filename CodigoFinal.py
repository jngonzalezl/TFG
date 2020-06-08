#TFG16 + OPTIMIZADO + adaptado a la nueva experimentacion

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


archivos = []
d = "./Documents/Experimentacion"
for path in os.listdir(d):
    full_path = os.path.join(d, path)
    if os.path.isfile(full_path):
        archivos.append(full_path)

#print(archivos)

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



#uno
punoPorcFin = float(uno[len(uno)-1]) # Para coger el ultimo porcentaje, porq cuando no esta duplica el ultimo porcentaje
for p in range(len(uno)):
    punoF = float(uno[p])
    if (punoF != 0.0) and (len(startpoints)==0):
        startpoints.append(p + 1)

    if (len(startpoints) != 0) and (len(finpoints) == 0):
        porcentajes.append(punoF)


    if punoF == punoPorcFin and len(finpoints) == 0 and len(startpoints) != 0: 
        #Para dejar el primer valor que coincida, x eso es 2
        finpoints.append(p + 2)

totalPoints.append(finpoints[0]-startpoints[0])

#dos
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

#tres
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

#cuatro
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

#cinco
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

#seis
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

#siete
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

#ocho
pochoPorcFin = float(ocho[len(ocho)-1]) # Para coger el ultimo porcentaje, porq cuando no esta duplica el ultimo porcentaje
for p in range(len(ocho)):
    pochoF = float(ocho[p])
    if (pochoF != 0.0) and (len(startpoints)==7):
        startpoints.append(p + 1)

    if (len(startpoints) != 7) and (len(finpoints) == 7):
        porcentajes.append(pochoF)


    if pochoF == pochoPorcFin and len(finpoints) == 7 and len(startpoints) != 7: 
        #Para dejar el primer valor que coincida, x eso es 2
        finpoints.append(p + 2)

totalPoints.append(finpoints[7]-startpoints[7])

#nueve
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

#diez
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

#once
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

#doce
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

#trece
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

#catorce
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

#MEDIAS
MediaPuntoComienzo = DesvPuntoComienzo = 0
MediaPuntoFinal = DesvPuntoFinal = 0
MediaPuntosPor = DesvPuntosPor = 0

MediaPuntoComienzo = np.average(startpoints)
MediaPuntoComienzoRound = round(MediaPuntoComienzo)
DesvPuntoComienzo = statistics.stdev(startpoints) #ESTO SE SUPONE QUE ES DESVIACION ESTANDAR


MediaPuntoFinal = np.average(finpoints)
MediaPuntoFinalRound = round(MediaPuntoFinal)
DesvPuntoFinal = statistics.stdev(finpoints)


MediaPuntosPor = np.average(porcentajes)
DesvPuntosPor = statistics.stdev(porcentajes)


######PRINTS
print("uno - Tamaño", len(uno))
print("dos - Tamaño", len(dos))
print("tres - Tamaño", len(tres))
print("cuatro - Tamaño", len(cuatro))
print("cinco - Tamaño", len(cinco))
print("seis - Tamaño", len(seis))
print("siete - Tamaño", len(siete))
print("ocho - Tamaño", len(ocho))
print("nueve - Tamaño", len(nueve))
print("diez - Tamaño", len(diez))
print("once - Tamaño", len(once))
print("doce - Tamaño", len(doce))
print("trece - Tamaño", len(trece))
print("catorce - Tamaño", len(catorce))

print("Media tamaño total experimentacion: ", MediaSizeTotal)
print("Tamaño total experimentacion: ", SizeTotal)

print()
print("uno - Aparece el objeto en el punto:", startpoints[0])
print("uno - Desaparece el objeto en el punto:", finpoints[0])
print("uno - Numero de puntos donde aparece el objeto" , totalPoints[0])
print()
print("dos - Aparece el objeto en el punto:", startpoints[1])
print("dos - Desaparece el objeto en el punto:", finpoints[1])
print("dos - Numero de puntos donde aparece el objeto" , totalPoints[1])
print()
print("tres - Aparece el objeto en el punto:", startpoints[2])
print("tres - Desaparece el objeto en el punto:", finpoints[2])
print("tres - Numero de puntos donde aparece el objeto" , totalPoints[2])
print()
print("cuatro - Aparece el objeto en el punto:", startpoints[3])
print("cuatro - Desaparece el objeto en el punto:", finpoints[3])
print("cuatro - Numero de puntos donde aparece el objeto" , totalPoints[3])
print()
print("cinco - Aparece el obejto en el punto:", startpoints[4])
print("cinco - Desaparece el objeto en el punto:", finpoints[4])
print("cinco - Numero de puntos donde aparece el objeto" , totalPoints[4])
print()
print("seis - Aparece el objeto en el punto:", startpoints[5])
print("seis - Desaparece el objeto en el punto:", finpoints[5])
print("seis - Numero de puntos donde aparece el objeto" , totalPoints[5])
print()
print("siete - Aparece el objeto en el punto:", startpoints[6])
print("siete - Desaparece el objeto en el punto:", finpoints[6])
print("siete - Numero de puntos donde aparece el objeto" , totalPoints[6])
print()
print("ocho - Aparece el objeto en el punto:", startpoints[7])
print("ocho - Desaparece el objeto en el punto:", finpoints[7])
print("ocho - Numero de puntos donde aparece el objeto" , totalPoints[7])
print()
print("nueve - Aparece el objeto en el punto:", startpoints[8])
print("nueve - Desaparece el objeto en el punto:", finpoints[8])
print("nueve - Numero de puntos donde aparece el objeto" , totalPoints[8])
print()
print("diez - Aparece el objeto en el punto:", startpoints[9])
print("diez - Desaparece el objeto en el punto:", finpoints[9])
print("diez - Numero de puntos donde aparece el objeto" , totalPoints[9])
print()
print("once - Aparece el objeto en el punto:", startpoints[10])
print("once - Desaparece el objeto en el punto:", finpoints[10])
print("once - Numero de puntos donde aparece el objeto" , totalPoints[10])
print()
print("doce - Aparece el obejto en el punto:", startpoints[11])
print("doce - Desaparece el objeto en el punto:", finpoints[11])
print("doce - Numero de puntos donde aparece el objeto" , totalPoints[11])
print()
print("trece - Aparece el objeto en el punto:", startpoints[12])
print("trece - Desaparece el objeto en el punto:", finpoints[12])
print("trece - Numero de puntos donde aparece el objeto" , totalPoints[12])
print()
print("catorce - Aparece el objeto en el punto:", startpoints[13])
print("catorce - Desaparece el objeto en el punto:", finpoints[13])
print("catorce - Numero de puntos donde aparece el objeto" , totalPoints[13])
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


import numpy as np
import matplotlib.pyplot as plt

FileAnormaly = open("./Documents/anormalyScore.txt", "w")
FileTrain = open("./Documents/DatawiTrainTri.txt", "w")
FileTest = open("./Documents/DatawiTestTri.txt", "w")
PtosTrain = open("./Documents/PuntosTrain.txt", "w")
PtosTest = open("./Documents/PuntosTest.txt", "w")

PtosTestCom = []
PtosTestFin = []



#CREACION PUNTOS TIEMPO COMIENZO
muTimeComTrain = MediaPuntoComienzoRound #1214
sigmaTimeComTrain = DesvPuntoComienzo #34.135584003179076 #desviacion estandar


numRTimeComTrain = 100 #xq es 1 mes

NPointsRTimeComTrain = []
pointsTimeComTrain = np.random.normal(muTimeComTrain, sigmaTimeComTrain, numRTimeComTrain)

for pt in range(len(pointsTimeComTrain)):
    pointRoundComTrain = round(pointsTimeComTrain[pt])
    NPointsRTimeComTrain.append(pointRoundComTrain)

NPointsRTimeSortedComTrain =sorted(NPointsRTimeComTrain)

print("Puntos time COM creados aplicando los filtros", NPointsRTimeSortedComTrain)
print("Tamaño array de puntos time COM con filtros", len(NPointsRTimeComTrain))
print()


#CREACION PUNTOS TIEMPO FINAL
DataTrainPor = []
DataTrain1 = []
DataTrainWi = []
DataTrainWiTiempo = []
DataTrainWiPunto = []

muTimeFinTrain = MediaPuntoFinalRound #1166
sigmaTimeFinTrain = DesvPuntoFinal #31.836636577556817
numRTimeFinTrain =  100

SizeTrains =10 #xq es 15 dias
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
while (i != SizeTrains):
    if (NPointsRTimeSortedComTrain[i] < NPointsRTimeSortedFinTrain[i]):
        NumTrain = i+1
        muPorTrain = MediaPuntosPor #0.7281953210091657
        sigmaPorTrain = DesvPuntosPor #0.04873312558172425

        print("--TRAIN--", NumTrain)
        print("Inicio:", NPointsRTimeSortedComTrain[i])
        print("Fin:", NPointsRTimeSortedFinTrain[i])
        PtosTrain.write(str(NPointsRTimeSortedComTrain[i]))
        PtosTrain.write(";")
        PtosTrain.write(str(NPointsRTimeSortedFinTrain[i]))
        PtosTrain.write(";")
        PtosTrain.write("\n")

        pointsTrain = NPointsRTimeSortedFinTrain[i] - NPointsRTimeSortedComTrain[i]
        pointsTrainI = int(pointsTrain)
        print("Numero de puntos TRAIN:", pointsTrainI)

        numRPorTrain = pointsTrainI
        pointsPorTrain = np.random.normal(muPorTrain, sigmaPorTrain, numRPorTrain)
        #print(pointsWi)

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
#print("Data train PORCENTAJES", DataTrainPor)
print("Tamaño TOTAL Data Train WI", len(DataTrainWi))
#print("Data train WI", DataTrainWi)
print("Tamaño TOTAL Data Train WI Tiempo", len(DataTrainWiTiempo))
#print("Data train WI", DataTrainWiTiempo)
print("Tamaño TOTAL Data Train WI Puntos", len(DataTrainWiPunto))
#print("Data train WI puntos", DataTrainWiPunto)



'''
plt.plot(DataTrainWi)
plt.title('Synthetic Data Training - Detection Breakfast')
#plt.title('Breakfast detection')
plt.axis([0, 54824, 0, 1])
plt.show()
'''

print(".....................................................................................................................................")
#CREACION DATA TEST

#CREACION PUNTOS TIEMPO COMIENZO

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

NPointsRTimeComTest = []
pointsTimeComTest =  np.random.randint(747.75, 1495.5, size=20) #low, high, size 6:00h -> 747.75, 12:00h -> 1495.5
                                                          
#print(pointsTimeComTest)

NPointsRTimeSortedComTest =sorted(pointsTimeComTest)

print("Puntos TEST time COM creados ordenados", NPointsRTimeSortedComTest)
#print("Tamaño TEST array de puntos time COM con filtros", len(NPointsRTimeSortedComTest))
print()



#print("Tamaño array de puntos time FIN con filtros", len(NPointsRTimeSortedFinTest))

SizeTests = (len(NPointsRTimeSortedComTest))
print("Voy a crear", SizeTests/2, "ficheros test")

pointsPorTest = []

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

    PtosTest.write(str(NPointsRTimeSortedComTest[i]))
    PtosTest.write(";")
    PtosTest.write(str(NPointsRTimeSortedFinTest))
    PtosTest.write(";")
    PtosTest.write("\n")

    ##UNA OPCION
    #pointsPorTest = np.random.random_sample((pointsTestI,))  ##sin filtro de 0.5
    ##
    #OTRA OPCION

    pointsPorT = np.random.random_sample((20000,))  ## + DE 0,5

    for r in range(len(pointsPorT)):
        if (pointsPorT[r] > 0.5) and (len(pointsPorTest) != pointsTestI):
            #print(pointsPorT[r])
            pointsPorTest.append(pointsPorT[r])


    ###
    print(len(pointsPorTest))

    for a in range(int(NPointsRTimeSortedComTest[i])):
        DataTestPor.append(0)
        DataTest1.append(0)

    for p in range(len(pointsPorTest)):
        DataTestPor.append(pointsPorTest[p])
        DataTest1.append(pointsPorTest[p])

    for p in range(3916 - int(NPointsRTimeSortedFinTest)): #es 3916 porq es el final
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
#print("Data train PORCENTAJES", DataTrainPor)
print("Tamaño TOTAL Data TEST WI", len(DataTestWi))
#print("Data test WI", DataTestWi)
print("Tamaño TOTAL Data TEST WI Tiempo", len(DataTestWiTiempo))
#print("Data test WI Tiempo", DataTestWiTiempo)
print("Tamaño TOTAL Data TEST WI Punto", len(DataTestWiPunto))
#print("Data test WI Punto", DataTestWiPunto)
print("Puntos test Com: ", PtosTestCom)
print("Puntos test Fin: ", PtosTestFin)

'''
plt.plot(DataTestWi)
plt.title('Synthetic Data Test - Detection Breakfast')
plt.axis([0, 7832, 0, 1])
plt.show()
'''


print(".....................................................................................................................................")
print("--SISTEMA DE ANOMALIAS--")


#Creo un array bidimensional, añadiendo cuanto tiempo dura que wi es mayor de 0.5
DataTestWiTiempoBi = np.zeros((len(DataTestWi), 2))
DataTrainWiTiempoBi = np.zeros((len(DataTrainWi), 2))

for a in range(len(DataTestWi)):
    DataTestWiTiempoBi[a][0] = DataTestWi[a]
    DataTestWiTiempoBi[a][1] = DataTestWiTiempo[a]

for a in range(len(DataTrainWi)):
    DataTrainWiTiempoBi[a][0] = DataTrainWi[a]
    DataTrainWiTiempoBi[a][1] = DataTrainWiTiempo[a]


#Creo un array bidimensional, añadiendo el punto en el que esta el valor wi
DataTestWiPuntoBi = np.zeros((len(DataTestWi), 2))
DataTrainWiPuntoBi = np.zeros((len(DataTrainWi), 2))

for a in range(len(DataTestWi)):
    DataTestWiPuntoBi[a][0] = DataTestWi[a]
    DataTestWiPuntoBi[a][1] = DataTestWiPunto[a]

for a in range(len(DataTrainWi)):
    DataTrainWiPuntoBi[a][0] = DataTrainWi[a]
    DataTrainWiPuntoBi[a][1] = DataTrainWiPunto[a]


#Creo un array tridimensional
DataTestWiTri = np.zeros((len(DataTestWi), 3))
DataTrainWiTri = np.zeros((len(DataTrainWi), 3))

for a in range(len(DataTestWi)):
    DataTestWiTri[a][0] = DataTestWi[a]
    DataTestWiTri[a][1] = DataTestWiPunto[a]
    DataTestWiTri[a][2] = DataTestWiTiempo[a]


for a in range(len(DataTrainWi)):
    DataTrainWiTri[a][0] = DataTrainWi[a]
    DataTrainWiTri[a][1] = DataTrainWiPunto[a]
    DataTrainWiTri[a][2] = DataTrainWiTiempo[a]
    val1 = str(DataTrainWi[a])
    val2 = str(DataTrainWiPunto[a])
    val3 = str(DataTrainWiTiempo[a])

    x1 = val1.replace('.',',')
    x2 = val2.replace('.',',')
    x3 = val3.replace('.',',')

    FileTrain.write(val1)
    FileTrain.write(";")
    FileTrain.write(val2)
    FileTrain.write(";")
    FileTrain.write(val3)
    FileTrain.write(";")
    FileTrain.write("\n")

for a in range(len(DataTestWi)):
    DataTestWiTri[a][0] = DataTestWi[a]
    DataTestWiTri[a][1] = DataTestWiPunto[a]
    DataTestWiTri[a][2] = DataTestWiTiempo[a]
    val1 = str(DataTestWi[a])
    val2 = str(DataTestWiPunto[a])
    val3 = str(DataTestWiTiempo[a])

    x1 = val1.replace('.',',')
    x2 = val2.replace('.',',')
    x3 = val3.replace('.',',')

    FileTest.write(val1)
    FileTest.write(";")
    FileTest.write(val2)
    FileTest.write(";")
    FileTest.write(val3)
    FileTest.write(";")
    FileTest.write("\n")


print("Media Train wi  -- ",np.average(DataTrainWi))
print("Media Train punto -- ",np.average(DataTrainWiPunto))
print("Media Train tiempo  -- ",np.average(DataTrainWiTiempo))


print("Media Test wi  -- ",np.average(DataTestWi))
print("Media Test punto -- ",np.average(DataTestWiPunto))
print("Media Test tiempo  -- ",np.average(DataTestWiTiempo))



#print(DataTestWi)
#print(DataTestWiTri)



import numpy as np
import rrcf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Data


print("TRAIN - Tamaño Wi", len(DataTrainWiTri))   
print("TEST - Tamaño Wi", len(DataTestWiTri))

datosUnidos = []

datosUnidos = np.append(DataTrainWi,DataTestWi)
print("Tamaño array datos unidos:", len(datosUnidos))

#Compruebo los días test para detectar las anomalias
#1º Comprobación --> que el punto de comienzo este entre 1064 y 1274
#2º Comprobación --> que el punto de fin este entre 1214 y 1354

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

# Set tree parameters
num_trees = 15
shingle_size = 5
tree_size = 10

# Create a forest of empty trees
forest = []
for _ in range(num_trees):
    tree = rrcf.RCTree()
    forest.append(tree)

# Use the "shingle" generator to create rolling window
pointsTrain = rrcf.shingle(DataTrainWiTri, size=shingle_size)
pointsTest = rrcf.shingle(DataTestWiTri, size=shingle_size)

# Create a dict to store anomaly score of each point
avg_codisp = {}
avg_codispTest = {}
#avg_codisp = np.zeros(len(datosUnidos))


def train (forest):
    print("TRAIN")
    # For each shingle... 
    for index, point in enumerate(pointsTrain):
        #print(index)
        # For each tree in the forest...
        for tree in forest:
            # Insert the new point into the tree
            #print("point train", point)
            tree.insert_point(point, index=index)
            # Compute codisp on the new point...
            new_codisp = tree.codisp(index)
            if not index in avg_codisp:
                avg_codisp[index] = 0
            # And take the average over all trees
            avg_codisp[index] += new_codisp / num_trees


    #print("Forest dentro de train",forest)
    


def test (forest):
    print("TEST")
    #print("Forest dentro de Test", forest)
    indexTrain = len(DataTrainWiTri)
    for index2, point2 in enumerate(pointsTest):   
        #print(index2) 
        for tree in forest:
            # Insert the new point into the tree
            tree.insert_point(point2, index=indexTrain)
            # Compute codisp on the new point...
            new_codisp = tree.codisp(indexTrain)
            #print("new_codisp", new_codisp)
            #print("point test", point2)
            # And take the average over all trees
            #print("index train", indexTrain)
            if not indexTrain in avg_codisp:
                
                avg_codispTest[index2] = 0
                avg_codisp[indexTrain] = 0

            avg_codisp[indexTrain] += new_codisp / num_trees
            avg_codispTest[index2] += new_codisp / num_trees
            #print(new_codisp / num_trees)

            #print("Antes de que se olvide el punto", forest)
            tree.forget_point(indexTrain)
            
        indexTrain= indexTrain + 1

    #print("Forest final borrados todos los puntos test", forest)

train(forest)
#print("Array codisp antes del test", avg_codisp)
test(forest)

#print("Array codisp despues del test", avg_codisp)
print(len(avg_codisp))

#print("Array codisp despues del test", avg_codisp)
print("Tamaño anormaly score total", len(avg_codisp))

print("Tamaño anormaly score test", len(avg_codispTest))

ptosAnomalias= []
for h in range(len(avg_codispTest)):
    if(avg_codispTest[h] > 0):
        ptosAnomalias.append(avg_codispTest[h])

#print(ptosAnomalias)
print("Total puntos detectados como anomalias:", len(ptosAnomalias) )
Acierto = (len(ptosAnomalias)/totalPtosAnomalia)*100
print("Acierto: ", Acierto)



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
