# 영상을 보고
# date_rows와 time_rows 리스트에 담겨있는 날짜와 시간 데이터를 이용하여
# 이중 for문과 문자열 합산을 통해 아래 예시 출력값과 같이
# 출력한 뒤 코드와 Console 창이 보이도록 캡쳐하여 올려주세요!

date_rows = ["20201123", "20201124", "20201125", "20201126", "20201127"]
time_rows = ["0900", "0930", "1000", "1030"]
min_rows = []

for a in date_rows:
    for b in time_rows:
        min_rows.append(a+b)

print(min_rows)
