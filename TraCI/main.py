import sys
from sumolib import checkBinary
import traci

def run():  # 所需要进行的操作就放在这里面
    step = 0
    while traci.simulation.getMinExpectedNumber() > 0:  # 意思就是还有车需要处理就处理
        traci.simulationStep()  # 仿真一步
        traci.tra
        step += 1
    traci.close()  # 仿真结束 关闭TraCI
    sys.stdout.flush()  # 清除缓冲区

if __name__ == "__main__":
    sumoBinary = checkBinary('sumo')  # 找到sumo的位置
    traci.start([sumoBinary, "-c", "xxx.sumocfg",
                             "--tripinfo-output", "tripinfo.xml"])
    # TraCI，启动！注意这里输出了仿真信息，保存为tripinfo.xml
    run()
