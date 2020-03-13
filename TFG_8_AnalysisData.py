#PORCENTAJES
import statistics
import numpy as np
lunes = []
martes = []
miercoles = []
jueves = []
viernes = []
sabado = []
domingo = []

startPointLunes = finPointLunes = totalPointLunes = 0
LunesPor = []
startPointMartes = finPointMartes = totalPointMartes = 0
MartesPor = []
startPointMiercoles = finPointMiercoles = totalPointMiercoles = 0
MiercolesPor = []
startPointJueves = finPointJueves = totalPointJueves = 0
JuevesPor = []
startPointViernes = finPointViernes = totalPointViernes = 0
ViernesPor = []
startPointSabado = finPointSabado = totalPointSabado = 0
SabadoPor = []
startPointDomingo = finPointDomingo = totalPointDomingo = 0
DomingoPor = []

with open("/Users/jennygonzalez/Documents/Experimentacion_TXT/Lunes_Experimentacion_2.txt", "r") as ins:
    for line in ins:
        #Dividamos la línea en una matriz llamada "campos" usando el ";" como separador:
        fields = line.split(";")
        #Extraemos el dato, en este caso "hamburger"
        lunes.append(fields[4])
        #5 --> wi de hamburger
        #4 --> porcentaje hamburger
        
with open("/Users/jennygonzalez/Documents/Experimentacion_TXT/Martes_Experimentacion_2.txt", "r") as ins:
    for line in ins:
        fields = line.split(";")
        martes.append(fields[4])

with open("/Users/jennygonzalez/Documents/Experimentacion_TXT/Miercoles_Experimentacion_2.txt", "r") as ins:
    for line in ins:
        fields = line.split(";")
        miercoles.append(fields[4])

with open("/Users/jennygonzalez/Documents/Experimentacion_TXT/Jueves_Experimentacion_2.txt", "r") as ins:
    for line in ins:
        fields = line.split(";")
        jueves.append(fields[4])

with open("/Users/jennygonzalez/Documents/Experimentacion_TXT/Viernes_Experimentacion_2.txt", "r") as ins:
    for line in ins:
        fields = line.split(";")
        viernes.append(fields[4])

with open("/Users/jennygonzalez/Documents/Experimentacion_TXT/Sabado_Experimentacion_2.txt", "r") as ins:
    for line in ins:
        fields = line.split(";")
        sabado.append(fields[4])

with open("/Users/jennygonzalez/Documents/Experimentacion_TXT/Domingo_Experimentacion_2.txt", "r") as ins:
    for line in ins:
        fields = line.split(";")
        domingo.append(fields[4])


print("LUNES - Tamaño", len(lunes))
print("MARTES - Tamaño", len(martes))
print("MIERCOLES - Tamaño", len(miercoles))
print("JUEVES - Tamaño", len(jueves))
print("VIERNES - Tamaño", len(viernes))
print("SABADO - Tamaño", len(sabado))
print("DOMINGO - Tamaño", len(domingo))

MediaSizeTotal = round((len(lunes) + len(martes) + len(miercoles) + len(jueves) + len(viernes) + len(sabado) + len(domingo))/7)
print("Media tamaño total experimentacion: ", MediaSizeTotal)

print()

#LUNES
pLunesPorcFin = float(lunes[len(lunes)-1]) # Para coger el ultimo porcentaje, porq cuando no esta duplica el ultimo porcentaje
for p in range(len(lunes)):
    #print(lunes[p])
    pLunesF = float(lunes[p])
    if (pLunesF != 0.0) and (startPointLunes == 0):
        startPointLunes = p + 1

    if (startPointLunes != 0) and (finPointLunes == 0):
        LunesPor.append(pLunesF)

    if pLunesF == pLunesPorcFin and finPointLunes == 0 and startPointLunes != 0: 
        finPointLunes = p + 2 #Para dejar el primer valor que coincida, x eso es 2



totalPointsLunes = finPointLunes - startPointLunes

print("LUNES - Aparece el objeto en el punto:", startPointLunes)
print("LUNES - Desaparece el objeto en el punto:", finPointLunes)
print("LUNES - Numero de puntos donde aparece el objeto" , totalPointsLunes)
print("LUNES - Puntos PORCENTAJES:" , len(LunesPor))
print()

#MARTES
pMartesPorcFin = float(martes[len(martes)-1])
for p in range(len(martes)):
    pMartesF = float(martes[p])
    if (pMartesF != 0.0) and (startPointMartes == 0):
        startPointMartes = p + 1
    
    if (startPointMartes != 0) and (finPointMartes == 0):
        MartesPor.append(pMartesF)

    if pMartesF == pMartesPorcFin and finPointMartes == 0 and startPointMartes != 0: 
        finPointMartes = p + 2
    


totalPointsMartes = finPointMartes - startPointMartes

print("MARTES - Aparece el objeto en el punto:", startPointMartes)
print("MARTES - Desaparece el objeto en el punto:", finPointMartes)
print("MARTES - Numero de puntos donde aparece el objeto" , totalPointsMartes)
print("MARTES - Puntos PORCENTAJE:" , len(MartesPor))
print()

#MIERCOLES
pMiercolesPorcFin = float(miercoles[len(miercoles)-1])
for p in range(len(miercoles)):
    pMiercolesF = float(miercoles[p])
    if (pMiercolesF != 0.0) and (startPointMiercoles == 0):
        startPointMiercoles = p + 1

    if (startPointMiercoles != 0) and (finPointMiercoles == 0):
        MiercolesPor.append(pMiercolesF)
    
    if pMiercolesF == pMiercolesPorcFin and finPointMiercoles == 0 and startPointMiercoles != 0: 
        finPointMiercoles = p + 2

totalPointsMiercoles = finPointMiercoles - startPointMiercoles

print("MIERCOLES - Aparece el objeto en el punto:", startPointMiercoles)
print("MIERCOLES - Desaparece el objeto en el punto:", finPointMiercoles)
print("MIERCOLES - Numero de puntos donde aparece el objeto" , totalPointsMiercoles)
print("MIERCOLES - Puntos PORCENTAJE:" , len(MiercolesPor))
print()

#JUEVES
pJuevesPorcFin = float(jueves[len(jueves)-1])
for p in range(len(jueves)):
    pJuevesF = float(jueves[p])
    if (pJuevesF != 0.0) and (startPointJueves == 0):
        startPointJueves = p + 1

    if (startPointJueves != 0) and (finPointJueves == 0):
        JuevesPor.append(pJuevesF)
    
    if pJuevesF == pJuevesPorcFin and finPointJueves == 0 and startPointJueves != 0: 
        finPointJueves = p + 2

totalPointsJueves = finPointJueves - startPointJueves

print("JUEVES - Aparece el objeto en el punto:", startPointJueves)
print("JUEVES - Desaparece el objeto en el punto:", finPointJueves)
print("JUEVES - Numero de puntos donde aparece el objeto" , totalPointsJueves)
print("JUEVES - Puntos PORCENTAJE:" , len(JuevesPor))
print()

#VIERNES
pViernesPorcFin = float(viernes[len(viernes)-1])
for p in range(len(viernes)):
    pViernesF = float(viernes[p])
    if (pViernesF != 0.0) and (startPointViernes == 0):
        startPointViernes = p + 1

    if (startPointViernes != 0) and (finPointViernes == 0):
        ViernesPor.append(pViernesF)

    if pViernesF == pViernesPorcFin and finPointViernes == 0 and startPointViernes != 0: 
        finPointViernes = p + 2

totalPointsViernes = finPointViernes - startPointViernes

print("VIERNES - Aparece el obejto en el punto:", startPointViernes)
print("VIERNES - Desaparece el objeto en el punto:", finPointViernes)
print("VIERNES - Numero de puntos donde aparece el objeto" , totalPointsViernes)
print("VIERNES - Puntos PORCENTAJE:" , len(ViernesPor))
print()

#SABADO
pSabadoPorcFin = float(sabado[len(sabado)-1])
for p in range(len(sabado)):
    pSabadoF = float(sabado[p])
    if (pSabadoF != 0.0) and (startPointSabado == 0):
        startPointSabado = p + 1

    if (startPointSabado != 0) and (finPointSabado == 0):
        SabadoPor.append(pSabadoF)        

    if pSabadoF == pSabadoPorcFin and finPointSabado == 0 and startPointSabado != 0: 
        finPointSabado = p + 2
totalPointSabado = finPointSabado - startPointSabado

print("SABADO - Aparece el objeto en el punto:", startPointSabado)
print("SABADO - Desaparece el objeto en el punto:", finPointSabado)
print("SABADO - Numero de puntos donde aparece el objeto" , totalPointSabado)
print("SABADO - Puntos PORCENTAJE:" , len(SabadoPor))
print()

#DOMINGO
pDomingoPorcFin = float(domingo[len(domingo)-1])
for p in range(len(domingo)):
    pDomingoF = float(domingo[p])
    if (pDomingoF != 0.0) and (startPointDomingo == 0):
        startPointDomingo = p + 1

    if (startPointDomingo != 0) and (finPointDomingo == 0):
        DomingoPor.append(pDomingoF)    

    if pDomingoF == pDomingoPorcFin and finPointDomingo == 0 and startPointDomingo != 0: 
        finPointDomingo = p + 2

totalPointDomingo = finPointDomingo - startPointDomingo

print("DOMINGO - Aparece el objeto en el punto:", startPointDomingo)
print("DOMINGO - Desaparece el objeto en el punto:", finPointDomingo)
print("DOMINGO - Numero de puntos donde aparece el objeto" , totalPointDomingo)
print("DOMINGO - Puntos PORCENTAJE:" , len(DomingoPor))

print()

#MEDIAS
MediaPuntoComienzo = DesvPuntoComienzo = 0
MediaPuntoFinal = DesvPuntoFinal = 0
MediaPuntosPor = DesvPuntosPor = 0

MediaPuntoComienzo = (startPointLunes + startPointMartes + startPointMiercoles + startPointJueves + startPointViernes + startPointSabado + startPointDomingo)/7
MediaPuntoComienzoRound = round(MediaPuntoComienzo)
DesvPuntoComienzo = statistics.stdev([startPointLunes, startPointMartes, startPointMiercoles, startPointJueves, startPointViernes, startPointSabado, startPointDomingo])

print("Media del punto donde aparece el objeto", MediaPuntoComienzoRound )
print("Desv del punto donde aparece el objeto", DesvPuntoComienzo )
print()


MediaPuntoFinal = (finPointLunes + finPointMartes + finPointMiercoles + finPointJueves + finPointViernes + finPointSabado + finPointDomingo)/7
MediaPuntoFinalRound = round(MediaPuntoFinal)
DesvPuntoFinal = statistics.stdev([finPointLunes, finPointMartes, finPointMiercoles, finPointJueves, finPointViernes, finPointSabado, finPointDomingo])

print("Media del punto donde desaparece el objeto", MediaPuntoFinalRound )
print("Desv del punto donde aparece el objeto", DesvPuntoFinal )
print()


MediaPuntosPor = (np.average(LunesPor) + np.average(MartesPor) + np.average(MiercolesPor) + np.average(JuevesPor) + np.average(ViernesPor)+ np.average(SabadoPor) + np.average(DomingoPor))/7
DesvPuntosPor = statistics.stdev([np.average(LunesPor), np.average(MartesPor), np.average(MiercolesPor), np.average(JuevesPor), np.average(ViernesPor), np.average(SabadoPor), np.average(DomingoPor)])
print("Media puntos Porcentaje:", MediaPuntosPor)
print("Desviacion puntos Porcentaje:", DesvPuntosPor)
print()
