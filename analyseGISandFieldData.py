import xlrd
wb=xlrd.open_workbook(r"I:\DataNScripts\Enterprise\awasvikas\fwdawasvikashpgdb\consumers_poles_building_NameGIS.xlsx")
sh=wb.sheet_by_name("Sheet4")

ACF=[]
for i in range(456):
    ACF.append(sh.cell_value(i+1,0))
ACF=set(ACF)
ACG=[]
for i in range(387):
    ACG.append(sh.cell_value(i+1,1))
ACG=set(ACG)
NA=[]
for g in ACG:
    if not (g in ACF):NA.append(g)

print len(NA)

NA=[]
for g in ACF:
    if not (g in ACG):NA.append(g)

print len(NA)

NA=[]
for g in ACF:
    if g in ACG:NA.append(g)

print len(NA)

shF=wb.sheet_by_name("field")
shG=wb.sheet_by_name("gis")
print "SCNO analysis"
scnF=[]
scnG=[]
import re

for i in range(456):
    cell=shF.cell_value(i+1,6)
    if cell!='':
        s=re.sub("^0+","",cell[3:])
        t=int(s)
    scnF.append(t)
scnF=set(scnF)
#s=scnF[1][3:]

#re.sub("^0+","",s)
for i in range(568):
    if shG.cell_value(i+1,8)!='':
        scnG.append(int(shG.cell_value(i+1,8)))
scnG=set(scnG)    
NA=[]
for g in scnG:
    if not (g in scnF):NA.append(g)

print len(NA)

NA=[]
for g in scnF:
    if not (g in scnG):NA.append(g)

print len(NA)

NA=[]
for g in scnF:
    if g in scnG:
        NA.append(g)

print len(NA)      

#for building id
print "Building ID Analysis"
bF=[]
bG=[]
#import re

for i in range(456):
    cell=shF.cell_value(i+1,19)
    if cell!='':
        #s=re.sub("^0+","",cell[3:])
        t=int(cell)
    bF.append(t)
bF=set(bF)
#s=scnF[1][3:]

#re.sub("^0+","",s)
for i in range(568):
    if shG.cell_value(i+1,10)!='':
        bG.append(int(shG.cell_value(i+1,10)))
bG=set(bG)    
NA=[]
for g in bG:
    if not (g in bF):NA.append(g)

print "ONLY G",len(NA)

NA=[]
for f in bF:
    if not (f in bG):NA.append(f)

print "ONLY F",len(NA)

NA=[]
for b in bF:
    if b in bG:
        NA.append(b)

print "BOTH",len(NA) 
    
#for poleID
print
"Pole ID Analysis"
pF=[]
pG=[]
#import re

for i in range(456):
    cell=shF.cell_value(i+1,20)
    if cell!='':
        #s=re.sub("^0+","",cell[3:])
        t=int(cell)
    pF.append(t)
pF=set(pF)
#s=scnF[1][3:]

#re.sub("^0+","",s)
for i in range(568):#actual568
    if shG.cell_value(i+1,9)!='':
        pG.append(int(shG.cell_value(i+1,9)))
pG=set(pG)    
NA=[]
for g in pG:
    if not (g in pF):NA.append(g)

print "ONLY G",len(NA)

NA=[]
for f in pF:
    if not (f in pG):NA.append(f)

print "ONLY F",len(NA)

NA=[]
for b in pF:
    if b in pG:
        NA.append(b)

print "BOTH",len(NA) 

#for Name
print "Name Analysis"
nF=[]
nG=[]
#import re

for i in range(456):
    cell=shF.cell_value(i+1,7)
    if cell!='':
        nF.append(cell)
#nF=set(nF)

for i in range(568):#actual568
    if shG.cell_value(i+1,9)!='':
        nG.append(shG.cell_value(i+1,15))
#nG=set(nG)    
NA=[]
for g in nG:
    if not (g in nF):NA.append(g)

print "ONLY G",len(NA)

NA=[]
for f in nF:
    if not (f in nG):NA.append(f)

print "ONLY F",len(NA)

NA=[]
for b in nF:
    if b in nG:
        NA.append(b)

print "BOTH",len(NA) 

#for mobile phone num
print "mobile number analysis"

#for poleID

pF=[]
pG=[]
#import re

for i in range(456):
    cell=shF.cell_value(i+1,3)
    if cell!='':
        #s=re.sub("^0+","",cell[3:])
        t=int(cell)
        pF.append(t)
pF=set(pF)
#s=scnF[1][3:]

#re.sub("^0+","",s)
for i in range(568):#actual568
    if shG.cell_value(i+1,5)!='':
        pG.append(int(shG.cell_value(i+1,5)))
pG=set(pG)    
NA=[]
for g in pG:
    if not (g in pF):NA.append(g)

print "ONLY G",len(NA)

NA=[]
for f in pF:
    if not (f in pG):NA.append(f)

print "ONLY F",len(NA)

NA=[]
for b in pF:
    if b in pG:
        NA.append(b)

print "BOTH",len(NA)
