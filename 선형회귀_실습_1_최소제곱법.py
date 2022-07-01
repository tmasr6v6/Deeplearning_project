import numpy as np

x = [2, 4, 6, 8]
y = [81, 93, 91, 97]

mx = np.mean(x)
my = np.mean(y)

print("x 원소들의 평군값: {}\ny 원소들의 평균값: {}".format(mx, my))



# 1) 기울기 공식 중 분모: x의 각 원소와 x의 평균 값들의 차를 제곱
divisor = sum([(i - mx)**2 for i in x])   # sum()은 시그마 기호에 해당하는 함수  /  ' for i in x '는 x의 각 원소를 한 번씩 i 자리에 대입하라는 의미


# 2) 이제 분자에 해당하는 값 구하기: x와 y의 편차를 곱해서 합한 값
def top(x, mx, y, my):
    d = 0                                         # 임의의 변수 d의 초기값을 0으로 설정
    for i in range(len(x)):                       # x의 개수만큼 실행
        d += (x[i] - mx) * (y[i] - my)
    return d

dividend = top(x, mx, y, my)


# 3) 위에서 구한 분모와 분자를 계산하여 기울기 a 구하기
a = dividend / divisor

# 4) y 절편 구하는 공식을 이용해, 회귀 상수 b 구하기
b = my - (mx * a)

# 결과물
print("분모: {}\n분자: {}\n기울기 a: {}\n상수 b: {}".format(divisor, dividend, a, b))