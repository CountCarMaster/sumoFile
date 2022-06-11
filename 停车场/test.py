from constants import GENERATE_DURATION, SIMULATE_DURATION, PARKING_MAXDUR, PARKING_MINDUR, CHECK_TIME, STABLE_TIME
from constants import PARKINGLOT_NUM_0, PARKINGLOT_NUM_1, PARKINGLOT_NUM_2
import numpy as np
from matplotlib import pyplot as plt

data1 = np.loadtxt("dataBefore.txt")
data2 = np.loadtxt("dataAfter.txt")
timeNum = int((SIMULATE_DURATION - STABLE_TIME) / CHECK_TIME)
beforeAve = np.mean(data1, axis = 1)
afterAve = np.mean(data2, axis = 1)

labels = ['','Road1_TravelTime', 'Road2_TravelTime', 'R3_TravelTime', 'Road1_QueueLength', 'Road2_QueueLength', 'Road3_QueueLength', 'P1_Occupation', 'P2_Occupation', "P3_Occupation"]
beforedata = beforeAve[1: 10]
afterdata = afterAve[1: 10]

for i in range(1, 10) :
    x = ['Before', "After"]
    y = [beforeAve[i], afterAve[i]]
    plt.title(labels[i])
    plt.bar(x, y)
    plt.show()
