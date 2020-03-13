import numpy as np
import matplotlib.pyplot as plt

puntosTest = []
#CREACION PUNTOS TIEMPO COMIENZO

muTimeCom = 1060
sigmaTimeCom = 34.135584003179076 #desviacion estandar
numRTimeCom = 10

NPointsRTimeCom = []
pointsTimeCom = np.random.normal(muTimeCom, sigmaTimeCom, numRTimeCom)

for pt in range(len(pointsTimeCom)):
    pointRoundCom = round(pointsTimeCom[pt])
    NPointsRTimeCom.append(pointRoundCom)

NPointsRTimeSortedCom =sorted(NPointsRTimeCom)

print("Puntos time COM creados aplicando los filtros", NPointsRTimeSortedCom)
print("Tamaño array de puntos time COM con filtros", len(NPointsRTimeCom))
print()


#CREACION PUNTOS TIEMPO FINAL
Test01Por = []
Test01= []
Test02Por = []
Test02 = []
Test03Por = []
Test03 = []
Test04Por = []
Test04 = []
Test05Por = []
Test05 = []
Test06Por = []
Test06 = []
Test07Por = []
Test07 = []
Test08Por = []
Test08 = []
Test09Por = []
Test09 = []
Test10Por = []
Test10 = []

muTimeFin = 1166
sigmaTimeFin = 31.351311964649295 
numRTimeFin = 10 

NPointsRTimeFin = []
pointsTimeFin = np.random.normal(muTimeFin, sigmaTimeFin, numRTimeFin)

for pt in range(len(pointsTimeFin)):
    pointRoundFin = round(pointsTimeFin[pt])
    NPointsRTimeFin.append(pointRoundFin)

NPointsRTimeSortedFin =sorted(NPointsRTimeFin)

print("Puntos time FIN creados aplicando los filtros", NPointsRTimeSortedFin)
print("Tamaño array de puntos time FIN con filtros", len(NPointsRTimeFin))

SizeTests = (len(NPointsRTimeSortedFin))
print("Voy a crear", SizeTests, "ficheros test")

for i in range(SizeTests):
    Numtest = i+1
    muPor = 0.7281953210091657
    sigmaPor = 0.04873312558172425

    if (Numtest == 1):
        print("--TEST--", Numtest)
        print("Inicio:", NPointsRTimeSortedCom[i])
        print("Fin:", NPointsRTimeSortedFin[i])
        pointsTest = NPointsRTimeSortedFin[i] - NPointsRTimeSortedCom[i]
        pointsTestI = int(pointsTest)
        print("Numero de puntos TEST:", pointsTestI)
        numRPor = pointsTestI
        pointsPor = np.random.normal(muPor, sigmaPor, numRPor)
        #print(pointsWi)

        for a in range(int(NPointsRTimeSortedCom[i])):
            Test01.append(0)

        for p in range(len(pointsPor)):
            #print(points[p])
            Test01Por.append(pointsPor[p])
            Test01.append(pointsPor[p])
        
        for p in range(3916 - int(NPointsRTimeSortedFin[i])):
            Test01.append(0)

    if (Numtest == 2):
        print("--TEST--", Numtest)
        print("Inicio:", NPointsRTimeSortedCom[i])
        print("Fin:", NPointsRTimeSortedFin[i])
        pointsTest = NPointsRTimeSortedFin[i] - NPointsRTimeSortedCom[i]
        pointsTestI = int(pointsTest)
        print("Numero de puntos TEST:", pointsTestI)
        numRPor = pointsTestI
        pointsPor = np.random.normal(muPor, sigmaPor, numRPor)
        #print(pointsWi)
        for a in range(int(NPointsRTimeSortedCom[i])):
            Test02.append(0)

        for p in range(len(pointsPor)):
            #print(points[p])
            Test02Por.append(pointsPor[p])
            Test02.append(pointsPor[p])
        
        for p in range(3916 - int(NPointsRTimeSortedFin[i])):
            Test02.append(0)

    if (Numtest == 3):
        print("--TEST--", Numtest)
        print("Inicio:", NPointsRTimeSortedCom[i])
        print("Fin:", NPointsRTimeSortedFin[i])
        pointsTest = NPointsRTimeSortedFin[i] - NPointsRTimeSortedCom[i]
        pointsTestI = int(pointsTest)
        print("Numero de puntos TEST:", pointsTestI)
        numRPor = pointsTestI
        pointsPor = np.random.normal(muPor, sigmaPor, numRPor)
        #print(pointsWi)
        for a in range(int(NPointsRTimeSortedCom[i])):
            Test03.append(0)

        for p in range(len(pointsPor)):
            #print(points[p])
            Test03Por.append(pointsPor[p])
            Test03.append(pointsPor[p])
        
        for p in range(3916 - int(NPointsRTimeSortedFin[i])):
            Test03.append(0)

    if (Numtest == 4):
        print("--TEST--", Numtest)
        print("Inicio:", NPointsRTimeSortedCom[i])
        print("Fin:", NPointsRTimeSortedFin[i])
        pointsTest = NPointsRTimeSortedFin[i] - NPointsRTimeSortedCom[i]
        pointsTestI = int(pointsTest)
        print("Numero de puntos TEST:", pointsTestI)
        numRPor = pointsTestI
        pointsPor = np.random.normal(muPor, sigmaPor, numRPor)
        #print(pointsWi)
        for a in range(int(NPointsRTimeSortedCom[i])):
            Test04.append(0)

        for p in range(len(pointsPor)):
            #print(points[p])
            Test04Por.append(pointsPor[p])
            Test04.append(pointsPor[p])
        
        for p in range(3916 - int(NPointsRTimeSortedFin[i])):
            Test04.append(0)

    if (Numtest == 5):
        print("--TEST--", Numtest)
        print("Inicio:", NPointsRTimeSortedCom[i])
        print("Fin:", NPointsRTimeSortedFin[i])
        pointsTest = NPointsRTimeSortedFin[i] - NPointsRTimeSortedCom[i]
        pointsTestI = int(pointsTest)
        print("Numero de puntos TEST:", pointsTestI)
        numRPor = pointsTestI
        pointsPor = np.random.normal(muPor, sigmaPor, numRPor)
        #print(pointsWi)
        for a in range(int(NPointsRTimeSortedCom[i])):
            Test05.append(0)

        for p in range(len(pointsPor)):
            #print(points[p])
            Test05Por.append(pointsPor[p])
            Test05.append(pointsPor[p])
        
        for p in range(3916 - int(NPointsRTimeSortedFin[i])):
            Test05.append(0)

    if (Numtest == 6):
        print("--TEST--", Numtest)
        print("Inicio:", NPointsRTimeSortedCom[i])
        print("Fin:", NPointsRTimeSortedFin[i])
        pointsTest = NPointsRTimeSortedFin[i] - NPointsRTimeSortedCom[i]
        pointsTestI = int(pointsTest)
        print("Numero de puntos TEST:", pointsTestI)
        numRPor = pointsTestI
        pointsPor = np.random.normal(muPor, sigmaPor, numRPor)
        #print(pointsWi)
        for a in range(int(NPointsRTimeSortedCom[i])):
            Test06.append(0)

        for p in range(len(pointsPor)):
            #print(points[p])
            Test06Por.append(pointsPor[p])
            Test06.append(pointsPor[p])
        
        for p in range(3916 - int(NPointsRTimeSortedFin[i])):
            Test06.append(0)

    if (Numtest == 7):
        print("--TEST--", Numtest)
        print("Inicio:", NPointsRTimeSortedCom[i])
        print("Fin:", NPointsRTimeSortedFin[i])
        pointsTest = NPointsRTimeSortedFin[i] - NPointsRTimeSortedCom[i]
        pointsTestI = int(pointsTest)
        print("Numero de puntos TEST:", pointsTestI)
        numRPor = pointsTestI
        pointsPor = np.random.normal(muPor, sigmaPor, numRPor)
        #print(pointsWi)
        for a in range(int(NPointsRTimeSortedCom[i])):
            Test07.append(0)

        for p in range(len(pointsPor)):
            #print(points[p])
            Test07Por.append(pointsPor[p])
            Test07.append(pointsPor[p])
        
        for p in range(3916 - int(NPointsRTimeSortedFin[i])):
            Test07.append(0)

    if (Numtest == 8):
        print("--TEST--", Numtest)
        print("Inicio:", NPointsRTimeSortedCom[i])
        print("Fin:", NPointsRTimeSortedFin[i])
        pointsTest = NPointsRTimeSortedFin[i] - NPointsRTimeSortedCom[i]
        pointsTestI = int(pointsTest)
        print("Numero de puntos TEST:", pointsTestI)
        numRPor = pointsTestI
        pointsPor = np.random.normal(muPor, sigmaPor, numRPor)
        #print(pointsWi)
        for a in range(int(NPointsRTimeSortedCom[i])):
            Test08.append(0)

        for p in range(len(pointsPor)):
            #print(points[p])
            Test08Por.append(pointsPor[p])
            Test08.append(pointsPor[p])
        
        for p in range(3916 - int(NPointsRTimeSortedFin[i])):
            Test08.append(0)

    if (Numtest == 9):
        print("--TEST--", Numtest)
        print("Inicio:", NPointsRTimeSortedCom[i])
        print("Fin:", NPointsRTimeSortedFin[i])
        pointsTest = NPointsRTimeSortedFin[i] - NPointsRTimeSortedCom[i]
        pointsTestI = int(pointsTest)
        print("Numero de puntos TEST:", pointsTestI)
        numRPor = pointsTestI
        pointsPor = np.random.normal(muPor, sigmaPor, numRPor)
        #print(pointsWi)
        for a in range(int(NPointsRTimeSortedCom[i])):
            Test09.append(0)

        for p in range(len(pointsPor)):
            #print(points[p])
            Test09Por.append(pointsPor[p])
            Test09.append(pointsPor[p])
        
        for p in range(3916 - int(NPointsRTimeSortedFin[i])):
            Test09.append(0)

    if (Numtest == 10):
        print("--TEST--", Numtest)
        print("Inicio:", NPointsRTimeSortedCom[i])
        print("Fin:", NPointsRTimeSortedFin[i])
        pointsTest = NPointsRTimeSortedFin[i] - NPointsRTimeSortedCom[i]
        pointsTestI = int(pointsTest)
        print("Numero de puntos TEST:", pointsTestI)
        numRPor = pointsTestI
        pointsPor = np.random.normal(muPor, sigmaPor, numRPor)
        #print(pointsWi)
        for a in range(int(NPointsRTimeSortedCom[i])):
            Test10.append(0)

        for p in range(len(pointsPor)):
            #print(points[p])
            Test10Por.append(pointsPor[p])
            Test10.append(pointsPor[p])
        
        for p in range(3916 - int(NPointsRTimeSortedFin[i])):
            Test06.append(0)


print()

#print("TEST 01 - Puntos", Test01Por)
print("TEST 01 PORCENTAJES - Tamaño", len(Test01Por))
print("TEST 01 TOTAL - Tamaño", len(Test01))
print()
print("TEST 02 PORCENTAJES - Tamaño", len(Test02Por))
print("TEST 02 TOTAL - Tamaño", len(Test02))
print()
print("TEST 03 PORCENTAJES - Tamaño", len(Test03Por))
print("TEST 03 TOTAL - Tamaño", len(Test03))
print()
print("TEST 04 PORCENTAJES - Tamaño", len(Test04Por))
print("TEST 04 TOTAL - Tamaño", len(Test04))
print()
print("TEST 05 PORCENTAJES - Tamaño", len(Test05Por))
print("TEST 05 TOTAL - Tamaño", len(Test05))
print()
print("TEST 06 PORCENTAJES - Tamaño", len(Test06Por))
print("TEST 06 TOTAL - Tamaño", len(Test06))
print()
print("TEST 07 PORCENTAJES - Tamaño", len(Test07Por))
print("TEST 07 TOTAL - Tamaño", len(Test07))
print()
print("TEST 08 PORCENTAJES - Tamaño", len(Test08Por))
print("TEST 08 TOTAL - Tamaño", len(Test08))
print()
print("TEST 09 PORCENTAJES - Tamaño", len(Test09Por))
print("TEST 09 TOTAL - Tamaño", len(Test09))
print()
print("TEST 10 PORCENTAJES - Tamaño", len(Test10Por))
print("TEST 10 TOTAL - Tamaño", len(Test10))

#TENGO QUE METERLE LOS 0 DE ALANTE Y DE DETRAS
#plt.plot(Test01Por)
#plt.title('TEST UNICAMENTE CUANDO ESTA EL OBJETO')
#plt.axis([0, 200, 0, 1])
#plt.show()


plt.plot(Test01)
plt.title('TEST 1 TOTAL')
plt.axis([0, 3916, 0, 1])
plt.show()

plt.plot(Test02)
plt.title('TEST 2 TOTAL')
plt.axis([0, 3916, 0, 1])
plt.show()

#ahora tengo que añadir 0 en los puntos restantes, he hecho que el array depuntos sea de 0 a 3916 (MediaSizeTotal)



'''
#CREACION PUNTOS RANDOM (WI)
#------- INFO --------
# PUNTOS SEMANA EXPERIMENTACION (DONDE ESTA LA HAMBURGUESA): 108, 97, 102, 96, 101, 97, 142| Por eso numR = 105

muWi = 0.9 #media (Donde es el pico mas alto en el eje X - linea roja) (Donde suelen estar todos los valores)
sigmaWi = 0.1 #desviacion estandar (Lo que varia sobre la media los demas valores)
numRWi = 500 #Numero de valores aleatorios q se crean (PONGO DE MAS PORQUE GENERAN VALORES SUPERIORES A 105)

NPointsRWi = []
pointsWi = np.random.normal(muWi, sigmaWi, numRWi)
#print(points)
for p in range(len(pointsWi)):
    #print(points[p])
    if pointsWi[p] < 1 and pointsWi[p] > 0.6 and len(NPointsRWi) != 10: 
        NPointsRWi.append(pointsWi[p])

print("Puntos Wi creados aplicando los filtros", NPointsRWi)
print("Tamaño array de puntos Wi con filtros", len(NPointsRWi))

'''