import pandas as pd
import psutil
import os
import time

def main():
    f = open('D:\\pythonPr\input\\UFLEX70-AMKOR_FT_CARMEL-EMS_A0_UF_REV3B_ft_x4_T8V727.00.1.AM_Jan30_0152_35_FT1_0.data', 'r') #data파일 읽어오기
    lines = f.readlines() #한줄마다 list에 저장
    f.close()

    lot=[] #필요한 list 생성
    lid=[]
    lotno=[]
    waferID=[]
    coordinatesX=[]
    coordinatesY=[]
    lidID=[]
    timestart=[]
    timeend=[]
    timestartTmp=[]
    timeendTmp=[]


    for i in lines:     #각 줄마다 탐색하면서 특정 문장이 존재한다면 각 list에 저장
        if i.startswith("ULT_read_ULT_site")==True:
            lot.append(i)#LotNo,WaferID,coordinatesX,coordinatesY 정보가 담겨있는 문장 list 저장
        if i.startswith("barcode site")==True:
            lid.append(i)#lidID 정보가 담겨있는 문장 list 저장
        if i.startswith("Time_Stamp_Start")==True:
            timestartTmp.append(i)#Time start 정보가 담겨있는 문장 list 저장
        if i.startswith("Time_Stamp_End")==True:
            timeendTmp.append(i)#Time end 정보가 담겨있는 문장 list 저장

    for j in lot:   #lot list에 저장된 문장을 '_'기준으로 나눈 뒤, LotNo,WaferID,coordinatesX,coordinatesY 각각 list에 추가
        word0=j.split('_')[6]
        lotno.append(word0)
        word1=j.split('_')[6]
        word2=j.split('_')[7]
        word3=word1+'_'+word2
        waferID.append(word3)
        word4=j.split('_')[8]
        coordinatesX.append(word4)
        word5=j.split('_')[9]
        new_word5=word5.split('\n')[0]  #문장 끝부분 줄바꾸기기 문장 삭제를 위함
        coordinatesY.append(new_word5)

    for x in lid:  #lid list에 저장된 문장을 '_'기준으로 나눈 뒤, LidIDl list에 추가
        word6=x.split(':')[1]
        new_word6=word6.split('\n')[0]
        if len(new_word6)<24:#lidID 정보가 포함된 문장 보다 긴 예외 데이터를 걸러내기 위한 작업
            lidID.append(new_word6)

    for y in timestartTmp:  #time 관련된 문장을 '_'으로 나눈 뒤, start&end list 추가
        word7=y.split('_')[9]
        new_word7=word7.split('\n')[0]
        timestart.append(new_word7)
    for z in timeendTmp:
        word8=z.split('_')[9]
        new_word8=word8.split('\n')[0]
        timeend.append(new_word8)


# 판다스를 이용하여 list를 column화 하여 정리
    df1=pd.DataFrame(lotno, columns=['LotNo'])
    df2=pd.DataFrame(waferID, columns=['WaferID'])
    df3=pd.DataFrame(coordinatesX, columns=['CoordinatesX'])
    df4=pd.DataFrame(coordinatesY, columns=['CoordinatesY'])
    df5=pd.DataFrame(lidID, columns=['LidID'])
    df6=pd.DataFrame(timestart, columns=['TimeStart'])
    df7=pd.DataFrame(timeend, columns=['TimeEnd'])

    result = pd.concat([df1,df2,df3,df4,df5,df6,df7],axis=1)    #가로를 기준으로 각 데이터프레임 하나로 합치기
    result.to_csv(r"D:\pythonPr\output\data.csv", index=False) #csv로 추출



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
