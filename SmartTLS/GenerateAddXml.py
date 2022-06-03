from Constants import PREFIX

tls = open('%s.add.xml' % PREFIX, "w")
print('<additional>', file = tls)
print('    <e1Detector id="De0" lane="e2to0_0" pos="450" freq="30" file="cross.out" friendlyPos="x"/>', file = tls)
print('    <laneAreaDetector id="De1" lane="e1to0_0" pos="300" endPos="492.8" file="cr1.out" freq="30" friendlyPos="x"/>', file = tls)
print('    <laneAreaDetector id="De1" lane="e3to0_0" pos="300" endPos="492.8" file="cr2.out" freq="30" friendlyPos="x"/>', file = tls)
print('</additional>', file = tls)
tls.close()





