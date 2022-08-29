import pandas as pd
import glob
import os
import psutil


def main():
    f = open('D:\\pythonPr\input\\UFLEX70-AMKOR_FT_CARMEL-EMS_A0_UF_REV3B_ft_x4_T8V727.00.1.AM_Jan30_0152_35_FT1_0.data', 'r') #data파일 읽어오기
    lines = f.readlines()   #한줄씩 리스트화

    i=0
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

    while i<len(lines): #각 줄마다 인덱스를 설정하여 마지막 인덱스 까지 탐색
        if lines[i]=="ULT_read: --- Executing: ULT_read\n": #LOT,WaferID,Coordinates 정보가 담겨있는 문장 바로 위와 일치하는 부분 인덱스 탐색
            a.append(i)#해당 인덱스 a list에 추가
            lot_index.append(i+1)#해당 인덱스에서 +8줄까지의 인덱스 list 추가
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


    for j in lot_index:#탐색한 인덱스를 바탕으로 내용 list에 추가
        lotTmp.append(lines[j])
    for k in lid_index:
        lidTmp.append(lines[k])


    for o in lotTmp:#인덱스를 통해 1차 정리된 List를 통해 아래 문장을 포함한 list 추가
        if o.startswith("ULT_read_ULT_site")==True:
            lot.append(o)
    for p in lidTmp:
        if p.startswith("barcode site")==True:
            lid.append(p)
    for s in lines:
        if s.startswith("Time_Stamp_Start")==True:
            timestartTmp.append(s)
        if s.startswith("Time_Stamp_End")==True:
            timeendTmp.append(s)


    for e in lot:#'_'를 기준으로 문장을 나눠 해당 정보 List에 저장
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


#판다스를 이용해 데이터프레임 생성
    df1=pd.DataFrame(lotno, columns=['LotNo'])
    df2=pd.DataFrame(waferID, columns=['WaferID'])
    df3=pd.DataFrame(coordinatesX, columns=['CoordinatesX'])
    df4=pd.DataFrame(coordinatesY, columns=['CoordinatesY'])
    df5=pd.DataFrame(lidID, columns=['LidID'])
    df6=pd.DataFrame(timestart, columns=['TimeStart'])
    df7=pd.DataFrame(timeend, columns=['TimeEnd'])

    result = pd.concat([df1,df2,df3,df4,df5,df6,df7],axis=1) #데이터프레임 합치기
    result.to_csv(r"D:\pythonPr\output\data.csv") #csv 추출


        # 메모리 측정을 위한 코드
    print("=="*20)
    print("== memory usage check")

    for exec_num in range(0, 2):
        # BEFORE code
        print(f"== {exec_num:2d} exec")
        # general RAM usage
        memory_usage_dict = dict(psutil.virtual_memory()._asdict())
        memory_usage_percent = memory_usage_dict['percent']
        print(f"BEFORE CODE: memory_usage_percent: {memory_usage_percent}%")
        # current process RAM usage
        pid = os.getpid()
        current_process = psutil.Process(pid)
        current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2.**20
        print(f"BEFORE CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")

        X = [i for i in range(0, 9000000)]
        # AFTER  code
        memory_usage_dict = dict(psutil.virtual_memory()._asdict())
        memory_usage_percent = memory_usage_dict['percent']
        print(f"AFTER  CODE: memory_usage_percent: {memory_usage_percent}%")
        # current process RAM usage
        pid = os.getpid()
        current_process = psutil.Process(pid)
        current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2.**20
        print(f"AFTER  CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")
        del X
        print("--"*30)

if __name__ == "__main__":
    main()







#ULT_read: --- Executing: ULT_read
