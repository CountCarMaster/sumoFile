import random
from Constants import SIMUTATION_TIME, PREFIX

random.seed(42)
pWE = 1.0 / 10
pEW = 1.0 / 11
pNS = 1.0 / 30
n = SIMUTATION_TIME

rous = open('%s.rou.xml' % PREFIX, "w")
print('<routes>', file = rous)
print('    <vType id="typeOnly" accel="0.8" decel="4.5" sigma="0.5" length="5" minGap="2.5" maxSpeed="16.67"/>', file = rous)
print('', file = rous)
print('    <route id="WE" edges="e5_1to1 e1to0 e0to3 e3to5_3"/>', file = rous)
print('    <route id="EW" edges="e5_3to3 e3to0 e0to1 e1to5_1"/>', file = rous)
print('    <route id="NS" edges="e5_2to2 e2to0 e0to4 e4to5_4"/>', file = rous)
print('', file = rous)

num = 0
for i in range(0, n) :
    if(random.uniform(0, 1) < pWE) :
        print('    <vehicle id="WE_%s" type="typeOnly" route="WE" depart="%s"/>' % (num, i), file = rous)
    if(random.uniform(0, 1) < pEW) :
        print('    <vehicle id="EW_%s" type="typeOnly" route="EW" depart="%s"/>' % (num, i), file = rous)
    if(random.uniform(0, 1) < pNS) :
        print('    <vehicle id="NS_%s" type="typeOnly" route="NS" depart="%s"/>' % (num, i), file = rous)
    num += 1
print("</routes>", file=rous)
rous.close()

