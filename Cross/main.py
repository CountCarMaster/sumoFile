def GenerateRouXml(path, period) :
    os.system(path + "randomTrips.py " + "-n cross.net.xml -o cross.trips.xml -b 0 -e 1000 -p " + str(period))
    os.system("duarouter -n cross.net.xml -t cross.trips.xml -o cross.rou.xml --ignore-errors")
    tree = ET.parse("cross.sumocfg")
    root = tree.getroot()
    for child in root :
        if(child.tag == 'output') :
            for child2 in child:
                child2.attrib['value'] = 'cross.output' + str(period) + '.xml'
    with open("cross.sumocfg", 'wb') as f :
        tree.write(f)
    os.system("sumo -c cross.sumocfg --device.fcd.period 100")


def DealOutputXml(period, num) :
    tree = ET.parse("cross.output" + str(period) + ".xml")
    root = tree.getroot()
    p = 0
    l = 0
    for child in root :
        if(child.attrib['time'] == "900.00") :
            for child2 in child :
                if(child2.tag == 'vehicle') :
                    p = p + 1
            speed = np.zeros(p)
            for child2 in child :
                if(child2.tag == 'vehicle') :
                    speed[l] = np.float(child2.attrib['speed'])
                    l = l + 1
    zer = np.where(speed < 1.0)
    ans = np.size(zer[0]) / p
    data[(0, num)] = period
    data[(1, num)] = ans


if __name__ == '__main__':
    import os
    import numpy as np
    import xml.etree.ElementTree as ET
    from decimal import *

    path = "/Users/gankutsuou/Desktop/tools/"
    num = 0
    now_num = 0
    for i in range(1, 21) :
        b = i * 0.05
        a = Decimal(b).quantize(Decimal('0.00'))
        GenerateRouXml(path, a)
        num += 1
    for i in range(2, 10) :
        GenerateRouXml(path, i)
        num += 1
    data = np.zeros((2, num))
    for i in range(1, 21) :
        b = i * 0.05
        a = Decimal(b).quantize(Decimal('0.00'))
        DealOutputXml(a, now_num)
        now_num += 1
    for i in range(2, 10) :
        DealOutputXml(i, now_num)
        now_num += 1
    np.savetxt("data.txt", data)
    os.system("python imageGenerate.py")

