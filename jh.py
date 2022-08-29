import pandas as pd
import psutil
import os
import time

def main():
    f = open('D:\\pythonPr\jh_input\\0000C1516FV~0000#.txt', 'r') #Raw 파일 읽어오기
    lines = f.readlines()
    f.close()

    str=[]
    tray=[]
    row=[]
    col=[]
    no=[]
    rejection=[]
    PKG_TH=[]
    TH_PCB=[]
    TH_Mold=[]
    SOH_ATN1_L=[]
    TH_ATN1_L=[]
    SOH_ATN1_R=[]
    TH_ATN1_R=[]
    SOH_ATN2_R=[]
    TH_ATN2_R=[]
    SOH_ATN3_R=[]
    TH_ATN3_R=[]
    SOH_ATN4_R=[]
    TH_ATN4_R=[]
    num=0

    for i in lines:#각 줄마다 탐색하면서 특정 문장이 존재한다면 각 list에 저장
        num=num+1
        if num>67:
            if i.startswith(" ---------------------------------")==True:
                break
            else:
                str.append(i)
    for k in str:
        if k.startswith("                     ")==True:
            str.remove(k)

    for j in str:
        word0=j.split('|')[0]
        tray.append(word0)
        word1=j.split('|')[1]
        row.append(word1)
        word2=j.split('|')[2]
        col.append(word2)
        word3=j.split('|')[3]
        no.append(word3)
        word4=j.split('|')[4]
        rejection.append(word4)
        word5=j.split('|')[5]
        PKG_TH.append(word5)
        word6=j.split('|')[6]
        TH_PCB.append(word6)
        word7=j.split('|')[7]
        TH_Mold.append(word7)
        word8=j.split('|')[8]
        SOH_ATN1_L.append(word8)
        word9=j.split('|')[9]
        TH_ATN1_L.append(word9)
        word10=j.split('|')[10]
        SOH_ATN1_R.append(word10)
        word11=j.split('|')[11]
        TH_ATN1_R.append(word11)
        word12=j.split('|')[12]
        SOH_ATN2_R.append(word12)
        word13=j.split('|')[13]
        TH_ATN2_R.append(word13)
        word14=j.split('|')[14]
        SOH_ATN3_R.append(word14)
        word15=j.split('|')[15]
        TH_ATN3_R.append(word15)
        word16=j.split('|')[16]
        SOH_ATN4_R.append(word16)
        word17=j.split('|')[17]
        new_word17=word17.split('\n')[0]
        TH_ATN4_R.append(new_word17)


    df1=pd.DataFrame(tray, columns=['Tray'])
    df2=pd.DataFrame(row, columns=['Row'])
    df3=pd.DataFrame(col, columns=['Col'])
    df4=pd.DataFrame(no, columns=['No'])
    df5=pd.DataFrame(rejection, columns=['Rejection'])
    df6=pd.DataFrame(PKG_TH, columns=['PKG_TH'])
    df7=pd.DataFrame(TH_PCB, columns=['TH_PCB'])
    df8=pd.DataFrame(TH_Mold, columns=['TH_Mold'])
    df9=pd.DataFrame(SOH_ATN1_L, columns=['SOH_ATN1_L'])
    df10=pd.DataFrame(TH_ATN1_L, columns=['TH_ATN1_L'])
    df11=pd.DataFrame(SOH_ATN1_R, columns=['SOH_ATN1_R'])
    df12=pd.DataFrame(TH_ATN1_R, columns=['TH_ATN1_R'])
    df13=pd.DataFrame(SOH_ATN2_R, columns=['SOH_ATN2_R'])
    df14=pd.DataFrame(TH_ATN2_R, columns=['TH_ATN2_R'])
    df15=pd.DataFrame(SOH_ATN3_R, columns=['SOH_ATN3_R'])
    df16=pd.DataFrame(TH_ATN3_R, columns=['TH_ATN3_R'])
    df17=pd.DataFrame(SOH_ATN4_R, columns=['SOH_ATN4_R'])
    df18=pd.DataFrame(TH_ATN3_R, columns=['TH_ATN3_R'])
    df19=pd.DataFrame(SOH_ATN4_R, columns=['SOH_ATN4_R'])
    df20=pd.DataFrame(TH_ATN4_R, columns=['TH_ATN4_R'])

    result = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19,df20],axis=1) #가로를 기준으로 각 데이터프레임 하나로 합치기
    result.to_csv(r"D:\pythonPr\jh_output\data3.csv", index=False) #csv로 추출

if __name__ == "__main__":
    main()
