# 입력으로 0에서 100사이의 정수값을 받아서
# 보스톤 주택 가격의 실제값과 예측값을 보여주는 프로그램
# 모델을 학습하지 않고 저장된 모델을 활용
# import part
import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model
import warnings
# 상수값 설정, 변수 초기화
seed = 2022
model_filename = 'boston.h5'
warnings.filterwarnings('ignore')
np.random.seed(2022)
boston = load_boston()
X_train, X_test, y_train, y_test = train_test_split(
    boston.data, boston.target, test_size = 0.1, random_state=seed
)
# 메인 모델 불러오기
model = load_model(model_filename)

# 메인
# 입력값을 받기
index = int(input("0 ~ 50 정수값을 입력하세요.> "))
test = X_test[index].reshape(1,-1)
pred_value = model.predict(test)
print(f'실제값 : {y_test[index]}, 예측값:{pred_value[0,0]:.2f}')
# 최종결과를 출력