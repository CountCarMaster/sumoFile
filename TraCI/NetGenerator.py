import os
import sys
from constant import PREFIX, DOUBLE_ROWS, ROW_DIST
import sumolib
import numpy as np

nodes = open("%s.nod.xml" % PREFIX, "w")
print("<nodes>", file = nodes)
edges = open("%s.edg.xml" % PREFIX, "w")
print("<edges>", file = edges)
'''
connections = open("%s.con.xml" % PREFIX, "w")
print("<connections>", file = connections)
'''

# Generate nod.xml
fx = np.array([0, 1, -1], dtype=int)
mem = np.zeros((9, 4), dtype=int)
numn = 0
for i in fx :
    for j in fx :
        print('    <node id="nd%s" x="%s" y="%s"/>' % (numn, i * ROW_DIST, j * ROW_DIST), file = nodes)
        mem[numn, 1] = numn
        mem[numn, 2] = i
        mem[numn, 3] = j
        numn += 1

print(mem)

#Generate edg.xml
for i in range(0, numn) :
    for j in range(i + 1, numn) :
        if(mem[i, 2] == mem[j, 2] - 1 and mem[i, 3] == mem[j, 3]) :
            print('    <edge id="nd%sto%s" from="nd%s" to="nd%s" numLanes="3" spreadType="center"/>' % (i, j, i, j), file = edges)
            print('    <edge id="-nd%sto%s" from="nd%s" to="nd%s" numLanes="3" spreadType="center"/>' % (i, j, j, i), file = edges)
        if(mem[i, 2] == mem[j, 2] + 1 and mem[i, 3] == mem[j, 3]) :
            print('    <edge id="nd%sto%s" from="nd%s" to="nd%s" numLanes="3" spreadType="center"/>' % (i, j, i, j), file=edges)
            print('    <edge id="-nd%sto%s" from="nd%s" to="nd%s" numLanes="3" spreadType="center"/>' % (i, j, j, i), file=edges)
        if(mem[i, 2] == mem[j, 2] and mem[i, 3] == mem[j, 3] - 1) :
            print('    <edge id="nd%sto%s" from="nd%s" to="nd%s" numLanes="3" spreadType="center"/>' % (i, j, i, j),
                  file=edges)
            print('    <edge id="-nd%sto%s" from="nd%s" to="nd%s" numLanes="3" spreadType="center"/>' % (i, j, j, i),
                  file=edges)
        if (mem[i, 2] == mem[j, 2] and mem[i, 3] == mem[j, 3] + 1):
            print('    <edge id="nd%sto%s" from="nd%s" to="nd%s" numLanes="3" spreadType="center"/>' % (i, j, i, j), file=edges)
            print('    <edge id="-nd%sto%s" from="nd%s" to="nd%s" numLanes="3" spreadType="center"/>' % (i, j, j, i), file=edges)

print("</nodes>", file = nodes)
print("</edges>", file = edges)
nodes.close()
edges.close()

os.system('netconvert --node-files=net.nod.xml --edge-files=net.edg.xml --output-file=map.net.xml')