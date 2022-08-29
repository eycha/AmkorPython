import pandas as pd
import timeit
import psutil
import os
import cProfile

# 파일 열기
f = open('D:\\pythonPr\input\\UFLEX70-AMKOR_FT_CARMEL-EMS_A0_UF_REV3B_ft_x4_T8V727.00.1.AM_Jan30_0152_35_FT1_0.data', 'r')
data = list(f.readlines())
f.close()

# 코드 실행 타이머 시작
start_time = timeit.default_timer()

def data_handling(d):
    # LotNo 추출
    LotNo = data[4].split()[1][:9]

    # Data List
    start_times = []
    end_times = []
    lid_ids = []
    wafer_info = []

    # 최종 Data_Log => csv
    data_logs = []

    # 코드 최적화 변수 - .append
    data_append = data_logs.append

    for i in d:
        # 공백제거
        strip_data = i.strip()

        # Start Time
        if strip_data.startswith('Time_Stamp_Start_'):
            start_times.append([strip_data.split('_')[7], strip_data.split('_')[9]])
            continue

        # End Time
        elif strip_data.startswith('Time_Stamp_End_'):
            end_times.append([strip_data.split('_')[7], strip_data.split('_')[9]])
            continue

        # Lid_ids
        elif strip_data.startswith('barcode'):
            lid_ids.append([strip_data.split(':')[0][-1], strip_data.split(':')[1]])
            continue

        # Wafer_id, x, y
        elif strip_data.startswith('ULT_read_'):
            wafer_info.append([strip_data.split('_')[4], '_'.join(strip_data.split('_')[6:8]), strip_data.split('_')[8], strip_data.split('_')[9]])

            continue

        # Device 별 데이터 결합 및 저장.
        elif wafer_info and strip_data.startswith('==='):
            for k in range(len(wafer_info)):
                data_log = [LotNo, 'Null', 'Null', 'Null', 'Null', 'Null', 'Null']
                site = wafer_info[k][0]
                print(site)
                for l in range(1, 4):
                    data_log[l] = wafer_info[k][l]
                data_log[4] = next((j[1] for j in lid_ids if j[0] == site))
                data_log[5] = next((j[1] for j in start_times if j[0] == site))
                sub_endtime = [j[1] for j in end_times if j[0] == site]
                data_log[6] = sub_endtime[0] if sub_endtime else 'Null'
                data_append(data_log)

            # 임시 리스트 리셋
            start_times = []
            end_times = []
            lid_ids = []
            wafer_info = []
    print(data_log)
    return data_logs
'''
# CPU, memory 사용량 확인
print("=="*20)
print("<memory usage check>")


# BEFORE code
# print(f"== {exec_num:2d} exec")
# general RAM usage
memory_usage_dict = dict(psutil.virtual_memory()._asdict())
memory_usage_percent = memory_usage_dict['percent']
print(f"BEFORE CODE: memory_usage_percent: {memory_usage_percent}%")
# current process RAM usage
pid = os.getpid()
current_process = psutil.Process(pid)
current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2. ** 20
print(f"BEFORE CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")


# 함수 실행
result = data_handling(data)


# AFTER  code
memory_usage_dict = dict(psutil.virtual_memory()._asdict())
memory_usage_percent = memory_usage_dict['percent']
print(f"AFTER  CODE: memory_usage_percent: {memory_usage_percent}%")
# current process RAM usage
pid = os.getpid()
current_process = psutil.Process(pid)
current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2. ** 20
print(f"AFTER  CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")
print("--" * 20)


# 코드 실행 타이머 종료
terminate_time = timeit.default_timer()
print("작업 시간 : %f sec" % (terminate_time - start_time))
print("--" * 20)
'''

# cProfile
cProfile.run( 'data_handling(data)' )


# 파일 저장
dataFrame = pd.DataFrame(result,
                         columns=['LotNo',
                                  'Wafer_id',
                                  'Coordinates_x',
                                  'Coordinates_y',
                                  'Lid_id',
                                  'Start_Time',
                                  'End_Time'])
dataFrame.to_csv("Final_Result.csv", header=True, index=False)
