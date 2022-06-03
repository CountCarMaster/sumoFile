import numpy as np
from Constants import BASIC_TIME, STEP
import matplotlib.pyplot as plt
import sys
from sumolib import checkBinary
import traci
from Constants import PREFIX
import os

def run(time) :
    step = 0
    maxlength = 0
    traci.trafficlight.setProgram("nd0", "%s" % time)
    traci.trafficlight.setPhase("nd0", 2)
    while traci.simulation.getMinExpectedNumber() > 0:  # 意思就是还有车需要处理就处理
        traci.simulationStep()  # 仿真一步
        maxlength = max(traci.lanearea.getJamLengthVehicle("De1"), traci.lanearea.getJamLengthVehicle("De2"), maxlength)
        if(traci.trafficlight.getPhase("nd0") == 2) :
            if(traci.inductionloop.getLastStepVehicleNumber("De0") > 0) :
                traci.trafficlight.setPhase("nd0", 3)
            else:
                traci.trafficlight.setPhase("nd0", 2)
        step += 1
        if(step > 5000) :
            maxlength = 100
            break
    traci.close()  # 仿真结束 关闭TraCI
    sys.stdout.flush()  # 清除缓冲区
    return maxlength

if __name__ == '__main__' :
    os.system('python GenerateAddXml.py')
    os.system('python GenerateRouXml.py')
    os.system('python GenerateSumocfg.py')
    os.system('python GenerateNetXml.py')
    sumoBinary = checkBinary('sumo')
    tabl = np.zeros((3, STEP))
    for i in range(0, STEP) :
        tabl[1, i] = BASIC_TIME + i
        traci.start([sumoBinary, "-c", "%s.sumocfg" % PREFIX, "--tripinfo-output", "tripinfo.xml"])
        tabl[2, i] = run(i + 1)
    ttime = tabl[1, :]
    queuee = tabl[2, :]
    plt.plot(ttime, queuee, marker = 'o')
    plt.xlabel("Interval")
    plt.ylabel("Length of Queue")
    plt.show()