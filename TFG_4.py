
#MIO
import numpy as np
import rrcf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Data

#Unos 102 cada uno
#Lunes
#datosTrain = [0.33606672, 0.4656633, 0.6337181, 0.6337181, 0.6337181, 0.6337181, 0.5027966, 0.5027966, 0.5027966, 0.48122862, 0.40358573, 0.30351374, 0.33877343, 0.90125483, 0.87973607, 0.8849676, 0.86559516, 0.8501008, 0.82689065, 0.82578295, 0.873693, 0.8307447, 0.8369593, 0.85175925, 0.85137904, 0.8453418, 0.8097256, 0.8200277, 0.83307385, 0.8503723, 0.83050436, 0.8395212, 0.816266, 0.8524213, 0.87576365, 0.823435, 0.81946766, 0.7925421, 0.8150884, 0.85538304, 0.8360874, 0.81630766, 0.8555697, 0.8166591, 0.7754525, 0.8257624, 0.8093147, 0.84519786, 0.86040974, 0.8319405, 0.8540771, 0.8574972, 0.85116816, 0.82038766, 0.8083297, 0.81278354, 0.8502671, 0.85692793, 0.8398858, 0.8598899, 0.81321234, 0.8260673, 0.8346043, 0.802473, 0.85406536, 0.8754743, 0.8113905, 0.85816157, 0.81485456,0.859456, 0.86021537, 0.7905524, 0.7820138, 0.82584643, 0.836056, 0.8216912, 0.8387175, 0.84270126, 0.81570345, 0.8509594, 0.8352825, 0.8819535, 0.8628144, 0.8648925, 0.8276506, 0.8612987, 0.83605134, 0.83655393, 0.8168185, 0.8239132, 0.78659457, 0.80774033, 0.8128576, 0.80901337, 0.7987822, 0.85332084, 0.84232, 0.8754192, 0.8661181, 0.8195907, 0.8641215, 0.8437294]
#Domingo
#datosTest  = [0.55641097, 0.48324126, 0.69972754, 0.4727365, 0.63689214, 0.63689214, 0.63689214, 0.33601388, 0.49189973, 0.49189973, 0.351647, 0.351647, 0.351647, 0.351647, 0.351647, 0.351647, 0.351647, 0.351647,0.351647, 0.351647, 0.351647, 0.351647, 0.351647, 0.351647, 0.351647, 0.351647, 0.351647, 0.351647, 0.351647, 0.31731904, 0.64756393, 0.64756393, 0.64756393, 0.4071339, 0.31008992, 0.31008992, 0.31008992, 0.31008992, 0.39885035, 0.39885035, 0.49947354, 0.39914718, 0.4114582, 0.4114582, 0.4114582, 0.4114582, 0.4114582, 0.4114582, 0.46521991, 0.8769837, 0.86516005, 0.82714903, 0.8617084, 0.857076, 0.87805086, 0.88417, 0.88034993, 0.8817994, 0.8532152, 0.8578145, 0.8811501, 0.85467565, 0.8750007, 0.8001659, 0.8183515, 0.8566807, 0.81954277, 0.8494839, 0.8675391, 0.867409, 0.89873767, 0.8317662, 0.84435546, 0.8854352, 0.82629925, 0.84731156, 0.84460455, 0.8368136, 0.85444766, 0.81096333, 0.87769175, 0.8409489, 0.8279599, 0.8186962, 0.8261237, 0.8673422, 0.84150845, 0.86430365, 0.85605824, 0.8179992, 0.86174953, 0.8697575, 0.8817399, 0.83386123, 0.8856173, 0.8587576, 0.86131245, 0.8172304, 0.88529235, 0.87338483, 0.86160535, 0.8780119]
#Martes
#datosTest2 = [0.42055628, 0.42055628, 0.39968815, 0.39968815, 0.5895393, 0.6190033, 0.5934097, 0.3856661, 0.472824, 0.5254541, 0.40301052, 0.6675103, 0.86854374, 0.3000059, 0.3000059, 0.44716933, 0.76298946, 0.86437684, 0.7924819, 0.8105262, 0.8461058, 0.8128226, 0.8395247, 0.8266176, 0.86274177, 0.8782682, 0.8394079, 0.7497554, 0.81828886, 0.73191214, 0.776374, 0.8592241, 0.7704612, 0.78660583, 0.74038434, 0.82443774, 0.76074934, 0.7872261, 0.8169342, 0.8447863, 0.8472222, 0.7701408, 0.7924603, 0.80136126, 0.8404302, 0.82649845, 0.796614, 0.88213974, 0.8193365, 0.8357692, 0.85241747, 0.87216, 0.86024064, 0.86123264, 0.8568717, 0.8195312, 0.8650347, 0.860664, 0.8272058, 0.7990947, 0.7536754, 0.83117574, 0.8320927, 0.79418916, 0.82310665, 0.8175584, 0.8277165, 0.8165886, 0.82551265, 0.76712525, 0.8155366, 0.7649136, 0.818934, 0.7850451, 0.72329813, 0.824645, 0.80873305, 0.7998531, 0.81608063, 0.8194401, 0.82909685, 0.8562663, 0.85617673, 0.8058554, 0.800379, 0.8321611, 0.798185, 0.83326656, 0.7906749, 0.78342956, 0.77252674, 0.73464286, 0.76360506, 0.8149454, 0.92776614, 0.92776614, 0.92776614, 0, 0, 0, 0 ,0]


#datosTrain = [0.33606672, 0.4656633, 0.6337181, 0.6337181, 0.6337181, 0.6337181, 0.5027966, 0.5027966, 0.5027966]
#datosTest  = [0.55641097, 0.48324126, 0.69972754, 0.4727365, 0.63689214, 0.63689214, 0.63689214, 0.33601388, 0.49189973]

#datosTrain = [0.33606672, 0.4656633]
#datosTest  = [0.55641097, 0.48324126]

datosTrain=[]

with open("/Users/jennygonzalez/Documents/trainHamburguesa.txt", "r") as ins:
    for line in ins:
        datosTrain.append(line)

print("Tamaño array train", len(datosTrain))
datosTest = []

with open("/Users/jennygonzalez/Documents/testHamburguesa.txt", "r") as ins:
    for line in ins:
        datosTest.append(line)

print("Tamaño array test", len(datosTest))

datosUnidos = []

datosUnidos = np.append(datosTrain,datosTest)

# Set tree parameters
num_trees = 1
shingle_size = 1
tree_size = 300

# Create a forest of empty trees
forest = []
for _ in range(num_trees):
    tree = rrcf.RCTree()
    forest.append(tree)

# Use the "shingle" generator to create rolling window
pointsTrain = rrcf.shingle(datosTrain, size=shingle_size)
pointsTest = rrcf.shingle(datosTest, size=shingle_size)

# Create a dict to store anomaly score of each point
avg_codisp = {}
#avg_codisp = np.zeros(len(datosUnidos))


def train (forest):
    print("TRAIN")
    # For each shingle... 
    for index, point in enumerate(pointsTrain):
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
    indexTrain = len(datosTrain)
    for index2, point2 in enumerate(pointsTest):    
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
                avg_codisp[indexTrain] = 0
            avg_codisp[indexTrain] += new_codisp / num_trees
            #print("Antes de que se olvide el punto", forest)
            tree.forget_point(indexTrain)

            
        indexTrain= indexTrain + 1

    #print("Forest final borrados todos los puntos test", forest)

train(forest)
#print("Array codisp antes del test", avg_codisp)
test(forest)

#print("Array codisp despues del test", avg_codisp)
print(len(avg_codisp))


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
ax2.set_ylim(0, 40)
plt.title('Data (red) and anomaly score (blue)', size=14)
plt.show()
