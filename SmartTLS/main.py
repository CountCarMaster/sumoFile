import numpy as np
from Constants import PREFIX
import sys
from sumolib import checkBinary
import traci
from Constants import PREFIX
import os

def run() :
    step = 0
    traci.trafficlight.setPhase("nd0", 2)
    while traci.simulation.getMinExpectedNumber() > 0:  # 意思就是还有车需要处理就处理
        traci.simulationStep()  # 仿真一步
        print(traci.lanearea.getJamLengthVehicle("De1"))
        if(traci.trafficlight.getPhase("nd0") == 2) :
            if(traci.inductionloop.getLastStepVehicleNumber("De0") > 0) :
                traci.trafficlight.setPhase("nd0", 3)
            else:
                traci.trafficlight.setPhase("nd0", 2)
        step += 1
    traci.close()  # 仿真结束 关闭TraCI
    sys.stdout.flush()  # 清除缓冲区

if __name__ == '__main__' :
    os.system('python GenerateNetXml.py')
    os.system('python GenerateAddXml.py')
    os.system('python GenerateRouXml.py')
    os.system('python GenerateSumocfg.py')
    sumoBinary = checkBinary('sumo')
    traci.start([sumoBinary, "-c", "%s.sumocfg" % PREFIX, "--tripinfo-output", "tripinfo.xml"])
    run()