import sys
from sumolib import checkBinary
import traci
from constants import GENERATE_DURATION, SIMULATE_DURATION, PARKING_MAXDUR, PARKING_MINDUR, CHECK_TIME, STABLE_TIME
from constants import PARKINGLOT_NUM_0, PARKINGLOT_NUM_1, PARKINGLOT_NUM_2
import random
import numpy as np

random.seed(42)

def run(sign):  # 所需要进行的操作就放在这里面
    num = 0
    data = np.zeros((10, 100000))
    timeNum = int((SIMULATE_DURATION - STABLE_TIME) / CHECK_TIME)
    nowNum = 0
    travelTime_0 = 0
    travelTime_1 = 0
    travelTime_2 = 0
    queueLength_0 = 0
    queueLength_1 = 0
    queueLength_2 = 0
    for step in range(0, SIMULATE_DURATION) :
        traci.simulationStep()
        if(step % GENERATE_DURATION == 0) :
            num += 1
            if(sign == 0) :
                random1 = int(random.uniform(1, 4))
            else :
                random1 = int(random.uniform(1, 3))
            PARKING_DURATION = random.uniform(PARKING_MINDUR, PARKING_MAXDUR)
            if(random1 == 1) :
                traci.vehicle.add("vhe%s" % num, "route1", typeID="type1")
                traci.vehicle.changeTarget("vhe%s" % num, "-105857812#4")
                traci.vehicle.setParkingAreaStop("vhe%s" % num, "pa_0", PARKING_DURATION)
            elif(random1 == 2) :
                traci.vehicle.add("vhe%s" % num, "route1", typeID="type1")
                traci.vehicle.changeTarget("vhe%s" % num, "105573433#1")
                traci.vehicle.setParkingAreaStop("vhe%s" % num, "pa_1", PARKING_DURATION)
            else :
                traci.vehicle.add("vhe%s" % num, "route1", typeID="type1")
                traci.vehicle.changeTarget("vhe%s" % num, "-438319551")
                traci.vehicle.setParkingAreaStop("vhe%s" % num, "pa_2", PARKING_DURATION)
            stop_vheID_0 = traci.parkingarea.getVehicleIDs("pa_0")
            for vhe in stop_vheID_0 :
                traci.vehicle.changeTarget(vhe, "-236665017#0")
            stop_vheID_1 = traci.parkingarea.getVehicleIDs("pa_1")
            for vhe in stop_vheID_1:
                traci.vehicle.changeTarget(vhe, "-236665017#0")
            stop_vheID_2 = traci.parkingarea.getVehicleIDs("pa_2")
            for vhe in stop_vheID_2:
                traci.vehicle.changeTarget(vhe, "-236665017#0")
        if(step >= STABLE_TIME - CHECK_TIME) :
            travelTime_0 += traci.edge.getTraveltime(traci.lane.getEdgeID(traci.parkingarea.getLaneID("pa_0")))
            travelTime_1 += traci.edge.getTraveltime(traci.lane.getEdgeID(traci.parkingarea.getLaneID("pa_1")))
            travelTime_2 += traci.edge.getTraveltime(traci.lane.getEdgeID(traci.parkingarea.getLaneID("pa_2")))
            queueLength_0 += traci.lanearea.getJamLengthVehicle("e2_0")
            queueLength_1 += traci.lanearea.getJamLengthVehicle("e2_1")
            queueLength_2 += traci.lanearea.getJamLengthVehicle("e2_2")
        if(step >= STABLE_TIME and int(step) % int(CHECK_TIME) == 0) :
            data[0, nowNum] = step
            data[1, nowNum] = (travelTime_0 / (CHECK_TIME * 1.0))
            data[2, nowNum] = (travelTime_1 / (CHECK_TIME * 1.0))
            data[3, nowNum] = (travelTime_2 / (CHECK_TIME * 1.0))
            data[4, nowNum] = (queueLength_0 / CHECK_TIME)
            data[5, nowNum] = (queueLength_1 / CHECK_TIME)
            data[6, nowNum] = (queueLength_2 / CHECK_TIME)
            data[7, nowNum] = (traci.parkingarea.getVehicleCount("pa_0") * 1.0) / (PARKINGLOT_NUM_0 * 1.0)
            data[8, nowNum] = (traci.parkingarea.getVehicleCount("pa_1") * 1.0) / (PARKINGLOT_NUM_1 * 1.0)
            data[9, nowNum] = (traci.parkingarea.getVehicleCount("pa_2") * 1.0) / (PARKINGLOT_NUM_2 * 1.0)
            travelTime_0 = 0
            travelTime_1 = 0
            travelTime_2 = 0
            queueLength_0 = 0
            queueLength_1 = 0
            queueLength_2 = 0
            nowNum += 1
    if(sign == 0) :
        np.savetxt("dataAfter.txt", data[:, 0:timeNum])
    else :
        np.savetxt("dataBefore.txt", data[:, 0:timeNum])
    traci.close()  # 仿真结束 关闭TraCI
    sys.stdout.flush()  # 清除缓冲区

if __name__ == "__main__":
    sumoBinary = checkBinary('sumo')  # 找到sumo的位置
    traci.start([sumoBinary, "-c", "map.sumocfg",
                             "--tripinfo-output", "tripinfo0.xml"])
    # TraCI，启动！注意这里输出了仿真信息，保存为tripinfo.xml
    run(0)
    traci.start([sumoBinary, "-c", "map.sumocfg",
                 "--tripinfo-output", "tripinfo1.xml"])
    run(1)