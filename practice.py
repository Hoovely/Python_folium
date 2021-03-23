def what_n(location):
    if location == '전국':
        return 224
    if location == '서울':
        return 25
    if location == '부산':
        return 16
    if location == '대구':
        return 8
    if location == '인천':
        return 10
    if location == '광주':
        return 5
    if location == '대전':
        return 5
    if location == '울산':
        return 5
    if location == '세종':
        return 1
    if location == '제주도':
        return 1
    if location == '경기도':
        return 31
    if location == '강원도':
        return 18
    if location == '충북':
        return 11
    if location == '충남':
        return 15
    if location == '전북':
        return 14
    if location == '전남':
        return 21
    if location == '경북':
        return 20
    if location == '경남':
        return 18
while 1:
    print("지자체를 입력하세요")
    where = str(input())
    n = what_n(where)
    name = []
    resis = []
    for i in range(n):
        name.append(str(input()))
    print("지자체 입력 완료")
    for i in range(n):
        resis.append(float(input()))
    print("저항성 값 입력 완료")

    raw_data = [[0,0] for _ in range(n)]
    for i in range(n):
        raw_data[i][0] = name[i]
        raw_data[i][1] = resis[i]
    print(raw_data)

# raw_data_전국_r2 = 
# raw_data_서울_r2 = 
# raw_data_부산_r2 = 
# raw_data_대구_r2 = 
# raw_data_인천_r2 = 
# raw_data_광주_r2 = 
# raw_data_대전_r2 = 
# raw_data_울산_r2 = 
# raw_data_세종_r2 =
# raw_data_제주_r2 = 
# raw_data_경기_r2 = 
# raw_data_충북_r2 = 
# raw_data_충남_r2 = 
# raw_data_전북_r2 = 
# raw_data_전남_r2 = 
# raw_data_경북_r2 =
# raw_data_경남_r2 = 

