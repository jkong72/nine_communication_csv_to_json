#판다스 라이브러리를 사용하여 과제를 해결하는 코드입니다.

import pandas as pd
import json
import os

sep = ' '+'-'*30

# 파일을 데이터프레임으로 읽기
file_directory = 'data/top20.csv'  # 파일 경로
top20_df = pd.read_csv(file_directory, encoding='utf-8')

# 결과 프린트
# print('데이터프레임'+sep)
# print(top20_df)

# 데이터프레임을 JSON 형식으로 변환
top20_json_string = pd.DataFrame.to_json(top20_df, orient='records', force_ascii=False)  # 한글 유니코드 깨짐 현상이 나타나므로 force_ascii=False 설정
top20_json = json.loads(top20_json_string)  # 문자열을 json 객체로 변환

# 결과 프린트
# print('json'+sep)
# print(top20_json)

# json데이터를 저장
os.mkdir('result')
output_directory = 'result/top20.json'  # 출력 경로
with open(output_directory, 'w', encoding='utf-8') as json_file:  # 인코딩 반드시 필요
    json_file.write(top20_json_string)

# 원하는 값만 파싱
# result = []
# for record in top20_json:
#     result.append(record['licenseOrgan'])

# 리스트 컴프리헨션을 사용한 코드
result = [record['licenseOrgan'] for record in top20_json]

# 결과 프린트
print('최종 결과'+sep)
print(result)