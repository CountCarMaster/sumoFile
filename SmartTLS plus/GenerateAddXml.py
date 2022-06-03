from Constants import PREFIX, BASIC_TIME, STEP

tls = open('%s.add.xml' % PREFIX, "w")
print('<additional>', file = tls)
print('    <e1Detector id="De0" lane="e2to0_0" pos="450" freq="30" file="cross.out" friendlyPos="x"/>', file = tls)
print('    <laneAreaDetector id="De1" lane="e1to0_0" pos="10" endPos="492.8" file="cr1.out" freq="30" friendlyPos="x"/>', file = tls)
print('    <laneAreaDetector id="De2" lane="e3to0_0" pos="10" endPos="492.8" file="cr2.out" freq="30" friendlyPos="x"/>', file = tls)
for i in range(1, STEP + 1) :
    print('    <tlLogic id="nd0" type="static" programID="%s" offset="0">' % i, file=tls)
    print('        <phase duration="%s" state="GrGr"/>' % (str)(BASIC_TIME + i - 1), file=tls)
    print('        <phase duration="3"  state="yryr"/>', file=tls)
    print('        <phase duration="30" state="rGrG"/>', file=tls)
    print('        <phase duration="3"  state="ryry"/>', file=tls)
    print('    </tlLogic>', file=tls)
print('</additional>', file = tls)
tls.close()





