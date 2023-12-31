
import os
import pandas as pd

# 스크립트가 있는 디렉토리
script_dir = os.path.dirname(os.path.abspath(__file__))

# CSV 파일 경로
csv_file = os.path.join(script_dir, 'data.csv')

# CSV 파일을 데이터프레임으로 읽어오기
df = pd.read_csv(csv_file)

while True:
    # 사용자로부터 입력 받은 단어
    input_word = input("飲みたいお酒を教えてください (退出するには「終了」を入力してください): ")

    if input_word == '終了':
        break

    # "name1" 및 "name2" 열에서 입력한 단어와 일치하는 행 찾기
    filtered_df = df[(df['name1'] == input_word) | (df['name2'] == input_word)]

    if not filtered_df.empty:
        # "food1" 열의 값을 가져오기
        foods1 = filtered_df['food1'].str.split(',').explode().str.strip()
        
        # 가장 많이 나타나는 상위 6개의 "food1" 찾기
        top_food1 = foods1.value_counts().head(6).index.tolist()
        
        # 상위 6개의 "food1"에 대한 평균 "month" 값을 계산
        avg_months = []
        for food in top_food1:
            avg_month = filtered_df[foods1 == food]['month'].mean()
            avg_months.append(avg_month)
        
        # "avg_months"를 기준으로 결과 정렬
        sorted_results = sorted(zip(top_food1, avg_months), key=lambda x: x[1])
        
        # 정렬된 결과 출력
        for food, avg_month in sorted_results:
            print(f"お勧めのおつまみ: {food}")
            print(f"時期: {round(avg_month)}月")
    else:
        print("申し訳ございません。まだ準備できていないお酒です。")
