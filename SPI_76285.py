import pandas as pd
import glob
import os

input_path = r'C:\test\input'
ouput_path = r'C:\test\ouput\result.csv'


cal = []

file_list = glob.(os.path.join(input_path,'K*'))
all_dataFrame = [] # 데이터 프레임을 저장할 빈 리시트를 하나 만든다.
for input_file in file_list:
    file_name = os.path.basename(input_file)
    df = pd.read_csv(input_file) # 판다스를 이용해서 csv파일을 읽는다.
    max_vol = df['Volume(%)'].max() # 판다스 구문으로 cost열을 불러 들이고 sum함수로 값을 더한다.
    min_vol = df['Volume(%)'].min()
    avg_vol = df['Volume(%)'].mean()
    std_vol = df['Volume(%)'].std(ddof=0)
    cpk1 = (180-avg_vol)/(3*std_vol)
    cpk2 = (avg_vol-25)/(3*std_vol)




    data = {'Max': [max_vol], 'Min': [min_vol], 'average': [avg_vol], 'std': [std_vol]}
    all_dataFrame.append(pd.DataFrame(data=data)) # data파일을 데이터 프레임으로 만들고 리스트에 저장한다.

All_data = pd.concat(all_dataFrame, axis=0, ignore_index=True) # 데이터 프레임들을 병합한다.
All_data.to_csv(output_file, index=False)
