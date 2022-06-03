import os
import sumolib
import numpy as np
from Constants import PREFIX, ROW_LENGTH, AVE_LENGTH

nodes = open("%s.nod.xml" % PREFIX, "w")
print("<nodes>", file = nodes)
edges = open("%s.edg.xml" % PREFIX, "w")
print("<edges>", file = edges)
connections = open("%s.con.xml" % PREFIX, "w")
print("<connections>", file = connections)

numm = 1
numx = np.array([0, -1, 0, 1, 0])
numy = np.array([0, 0, 1, 0, -1])

# Generate .nod.xml
print('    <node id="nd0" x="0" y="0" type="traffic_light"/>', file = nodes)
for i in range(1, 5) :
    print('    <node id="nd%s" x="%s" y="%s" type="priority"/>' % (numm, numx[numm] * ROW_LENGTH, numy[numm] * ROW_LENGTH), file = nodes)
    numm += 1
numm = 1
for i in range(1, 5) :
    print('    <node id="nd5_%s" x="%s" y="%s" type="priority"/>' % (numm, numx[numm] * (ROW_LENGTH + AVE_LENGTH), numy[numm] * (ROW_LENGTH + AVE_LENGTH)), file = nodes)
    numm += 1

# Generate .edg.xml
for i in range(1, 5) :
    print('    <edge id="e%sto0" from="nd%s" to="nd0" numLanes="1" speed="15"/>' % (i, i), file = edges)
    print('    <edge id="e0to%s" from="nd0" to="nd%s" numLanes="1" speed="15"/>' % (i, i), file = edges)
for i in range(1, 5) :
    print('    <edge id="e%sto5_%s" from="nd%s" to="nd5_%s" numLanes="1" speed="15"/>' % (i, i, i, i), file = edges)
    print('    <edge id="e5_%sto%s" from="nd5_%s" to="nd%s" numLanes="1" speed="15"/>' % (i, i, i, i), file = edges)

# Generate .con.xml
for i in range(1, 5) :
    fromEdge = i
    if(i + 2 > 4):
        toEdge = i - 2
    else :
        toEdge = i + 2
    print('    <connection from="e%sto0" to="e0to%s" fromLane="0" toLane="0"/>' % (fromEdge, toEdge), file = connections)
    print('    <connection from="e0to%s" to="e%sto5_%s" fromLane="0" toLane="0"/>' % (i, i, i), file = connections)
    print('    <connection from="e5_%sto%s" to="e%sto0" fromLane="0" toLane="0"/>' % (i, i, i), file = connections)
    print('    <connection from="e5_%sto%s" to="e%sto5_%s" fromLane="0" toLane="0"/>' % (i, i, i, i), file = connections)

# FinalWork
print('</nodes>', file = nodes)
nodes.close()
print('</edges>', file = edges)
edges.close()
print('</connections>', file = connections)
connections.close()

path = '/usr/local/Cellar/sumo/1.13.0/share/sumo/tools'
os.system('netconvert --node-files=cross.nod.xml --edge-files=cross.edg.xml --connection-files=cross.con.xml --output-file=cross.net.xml')