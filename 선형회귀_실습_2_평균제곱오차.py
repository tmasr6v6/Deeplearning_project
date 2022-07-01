import numpy as np

# 평균제곱오차를 파이썬으로 구현해보기

fake_a_b = [3, 76]   # 임의로 정한 '기울기 a'와 'y절편 b의 값'


data = [[2, 81], [4, 93], [6, 91], [8, 97]]   # 공부한 시간과 이에 따른 성적을 짝지은 리스트

x = [i[0] for i in data]     # x 리스트와 y 리스트를 만들어
y = [i[1] for i in data]     # 첫 번째 값을 x 리스트에 저장하고, 두 번째 값을 y 리스트에 저장


def predict(x):   # predict()라는 함수를 사용해, 일차방정식 y = ax + b를 구현
    return (fake_a_b[0] * x) + fake_a_b[1]


# MSE 함수(평균제곱오차 공식)
def mse(y, y_hat):
    return ((y - y_hat) ** 2).mean()


# mse_val(): mse() 함수에 데이터를 대입하여, 최종값을 구하는 함수
def mse_val(y, predict_result):
    return mse(np.array(y), np.array(predict_result))

# predict_result에는 앞서 만든 일차 방정식 함수 predict()의 결과값이 들어갑니다
# 이 값과 y값이 각각 예측값과 실제 값으로 mse()함수 안에 들어가게 됩니다.
# 이제 모든 x값을 predict()함수에 대입하여 예측 값을 구하고
# 이 예측 값과 실제 값을 통해, 최종값을 출력하는 코드를 다음과 같이 작성합니다.

predict_result = []    # 예측값이 들어갈 빈 리스트

for i in range(len(x)):                         # 모든 x값을 한 번씩 대입하여
    predict_result.append(predict(x[i]))        # 그 결과에 해당하는 predict_result 리스트를 완성
    print("공부시간 = %.f, 실제 점수 = %.f, 예측 점수 = %.f" % (x[i], y[i], predict(x[i])))


# 최종 MSE 출력
print("mse 최종값: " + str(mse_val(y, predict_result)))



# 이를 통해 처음에 가정한 a = 3, b = 76은 오차가 약 11.0이라는 것을 알게 됨
# 이제 남은 것은 이 오차를 줄이면서 새로운 선을 긋는 것: '경사하강법' 이용