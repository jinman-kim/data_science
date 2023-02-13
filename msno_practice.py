import pandas as pd
import numpy as np
import missingno as msno     #결측치
import matplotlib.pylab as plt  #  plot, 시각화
import seaborn as sns
from io import StringIO
from sklearn.impute import SimpleImputer

csv_data = StringIO("""
x1,x2,x3,x4,x5
1,0.1,"1",2019-01-01,A
2,,,2019-01-02,B
3,,"3",2019-01-03,C
,0.4,"4",2019-01-04,A
5,0.5,"5",2019-01-05,B
,,,2019-01-06,C
7,0.7,"7",,A
8,0.8,"8",2019-01-08,B
9,0.9,,2019-01-09,C
""")
df = pd.read_csv(csv_data, dtype={"x1": pd.Int64Dtype()}, parse_dates=[3])
print(df)
# msno.matrix(df) # 행렬 시각화
# msno.bar(df) # bar 모양 시각화
# plt.show() # 시각화

titanic = sns.load_dataset('titanic')  # seaborn 라이브러리 불러주삼

# msno.matrix(titanic)
# plt.show()
# print(titanic.tail())

titanic = titanic.dropna(thresh=int(len(titanic) * 0.5), axis=1)
msno.matrix(titanic)
# plt.show()

imputer = SimpleImputer(strategy='most_frequent')
df = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
print(df)
