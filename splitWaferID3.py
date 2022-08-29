import pandas as pd
import glob
import os

import time     # Check for Running Time
import psutil   # Check for Memory


# The Memory Usage before Running
print("<Before Running>")
memory_usage_dict = dict(psutil.virtual_memory()._asdict())
memory_usage_percent = memory_usage_dict['percent']
print(f"BEFORE CODE: memory_usage_percent: {memory_usage_percent}%")

pid = os.getpid()
current_process = psutil.Process(pid)
current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2. ** 20
print(f"BEFORE CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")

print("============================= \n")

start = time.time()

# 코드 작성란

end = time.time()
print("\n=============================")
print("<After Running>")
# MEMORY USAGE
memory_usage_dict = dict(psutil.virtual_memory()._asdict())
memory_usage_percent = memory_usage_dict['percent']
print(f"AFTER  CODE: memory_usage_percent: {memory_usage_percent}%")

pid = os.getpid()
current_process = psutil.Process(pid)
current_process_memory_usage_as_KB_ed = current_process.memory_info()[0] / 2.**20
print(f"AFTER  CODE: Current memory KB   : {current_process_memory_usage_as_KB_ed: 9.3f} KB")
print("")
print(f"Time: {end - start:.2f} sec")
print(f"Memory: {current_process_memory_usage_as_KB_ed - current_process_memory_usage_as_KB:.2f} KB")




f = open('D:\\pythonPr\input\\UFLEX70-AMKOR_FT_CARMEL-EMS_A0_UF_REV3B_ft_x4_T8V727.00.1.AM_Jan30_0152_35_FT1_0.data', 'r')
lines = f.readlines()


i=0
j=0
a=[]
lot_index=[]
lid_index=[]
lot=[]
lid=[]
lotno=[]
waferID=[]
coordinatesX=[]
coordinatesY=[]
lidID=[]
lotTmp=[]
lidTmp=[]
timestart=[]
timeend=[]
timestartTmp=[]
timeendTmp=[]

indexch1=[]
indexch2=[]
while i<len(lines):
    if lines[i]=="ULT_read: --- Executing: ULT_read\n":
        a.append(i)
        lot_index.append(i+1)
        lot_index.append(i+2)
        lot_index.append(i+3)
        lot_index.append(i+4)
        lid_index.append(i+5)
        lid_index.append(i+6)
        lid_index.append(i+7)
        lid_index.append(i+8)
        lid_index.append(i+9)
        lid_index.append(i+10)
    i=i+1


for j in lot_index:
    lotTmp.append(lines[j])
for k in lid_index:
    lidTmp.append(lines[k])


for o in lotTmp:
    if o.startswith("ULT_read_ULT_site")==True:
        lot.append(o)
for p in lidTmp:
    if p.startswith("barcode site")==True:
        lid.append(p)
n=1
for s in lines:
    if s.startswith("Time_Stamp_Start")==True:
        indexch1.append(lines.index(s))
        indexch2.append(indexch1[0])
        while n<len(indexch1):
            if n%4==0:
                indexch2.append(indexch1[n])

            n=n+1

        timestartTmp.append(s)
    if s.startswith("Time_Stamp_End")==True:
        timeendTmp.append(s)

print(indexch2)
'''

for e in lot:
    word0=e.split('_')[6]
    lotno.append(word0)

    word1=e.split('_')[6]
    word2=e.split('_')[7]
    word3=word1+'_'+word2
    waferID.append(word3)

    word4=e.split('_')[8]
    coordinatesX.append(word4)

    word5=e.split('_')[9]
    new_word5=word5.split('\n')[0]
    coordinatesY.append(new_word5)
for u in lid:
    word6=u.split(':')[1]
    new_word6=word6.split('\n')[0]
    if len(new_word6)<24:
        lidID.append(new_word6)
for d in timestartTmp:
    word7=d.split('_')[9]
    timestart.append(word7)
for g in timeendTmp:
    word8=g.split('_')[9]
    timeend.append(word8)



df1=pd.DataFrame(lotno, columns=['LotNo'])
df2=pd.DataFrame(waferID, columns=['WaferID'])
df3=pd.DataFrame(coordinatesX, columns=['CoordinatesX'])
df4=pd.DataFrame(coordinatesY, columns=['CoordinatesY'])
df5=pd.DataFrame(lidID, columns=['LidID'])
df6=pd.DataFrame(timestart, columns=['TimeStart'])
df7=pd.DataFrame(timeend, columns=['TimeEnd'])

result = pd.concat([df1,df2,df3,df4,df5,df6,df7],axis=1)
result.to_csv(r"D:\pythonPr\output\data.csv")



'''





#ULT_read: --- Executing: ULT_read
