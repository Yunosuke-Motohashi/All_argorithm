import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import csv
import numpy as np
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import GridSearchCV
import time
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from statistics import mean,median,variance,stdev

# データの読み込み
dataset= pd.read_csv('M:/UserDir/y_hcr_motohashi/Desktop/data_3/merge_0109.csv')
dataset = dataset.drop('Unnamed: 0', axis=1)
dataset=dataset.drop("OKYAKUSAMA2_NO", axis=1)
dataset=dataset.drop("OKYAKUSAMA3_NO", axis=1)
dataset=dataset.drop("TENKEN_ID", axis=1)
dataset=dataset.drop("date", axis=1)
dataset=dataset.drop("ZETSUKANSHIKENTAISHO_FLG", axis=1)
dd=dataset.drop_duplicates()
print('0109',len(dataset),len(dd))
dd.dtypes
dataset=dd

# データをラベルと入力データに分離する
target_col='MORE_AMP'
feature_col=dataset.columns.values
feature_col=feature_col.tolist()
feature_col.pop(1)
feature_col=np.array(feature_col)
print(feature_col)
y=np.array(dataset[target_col])
x=np.array(dataset[feature_col])

start = time.time()
# 学習用とテスト用に分離する
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)
print('Split End')

#フィッティング
etr = ExtraTreesRegressor(n_estimators=2500,bootstrap=True,n_jobs=1, random_state=0)
etr.fit(x_train, y_train)
print('fitting End')

#決定係数
r_train=etr.score(x_train,y_train)
r_test=etr.score(x_test, y_test)

#RMSE
y_train_pred= etr.predict(x_train)
y_test_pred = etr.predict(x_test)
mse_train=mean_squared_error(y_train, y_train_pred)
mse_test=mean_squared_error(y_test, y_test_pred)
rmse_train= np.sqrt(mse_train)
rmse_test= np.sqrt(mse_test)

#計算時間
elapsed_time = time.time() - start
print ("{0}".format(elapsed_time) + "[sec]")
print('r_train',r_train)
print('r_test',r_test)
print('rmse_train',rmse_train)
print('rmse_test',rmse_test)
print('R2,RMSE ExtraTrees End')
#変数重要度
fti = etr.feature_importances_   
print('Feature Importances:')
a=0
for i, feat in enumerate(feature_col):
    a=a+fti[i]
    print('\t{0:20s} : {1:>.6f}'.format(feat, fti[i]*100),a)

#gosa
list_gosa=[]
for i in range(len(y_test_pred)):
    test=y_test[i]
    pred=y_test_pred[i]
    gosa=y_test_pred[i]-y_test[i]
    list_gosa.append(gosa)
mean(list_gosa)


import matplotlib.pyplot as plt
a=len(y_test_pred)
list_1=[]
for i in range(a):
    b=y_test_pred[i]-y_test[i]
    list_1.append(b)

import collections
c = collections.Counter(list_gosa)
list_keys=[]
list_values=[]
for i in c.keys():
    list_keys.append(i)
    
for i in c.values():
    list_values.append(i)

df_dif=pd.DataFrame({ "Difference":list_keys, "Amount":list_values})
df_dif= df_dif.sort_values('Difference')
plt.bar(df_dif['Difference'], 
        df_dif['Amount'],
        color='lightblue', 
        align='center') 

max(list_gosa)
min(list_gosa)

list_1=[]
list_2=[]
for i in range(53305):
    a=5245-1*i
    b=5245-1*(i+1)+0.0000000001
    df_1=df_dif[df_dif["Difference"]<a]
    df_2=df_1[df_1["Difference"]>b]
    list_1.append(b)
    c=df_2["Amount"].sum()
    list_2.append(c)
df=pd.DataFrame({ "Difference":list_1, "Amount":list_2})    

df_dif.to_csv('M:/UserDir/y_hcr_motohashi/Desktop/data_3/result/extratrees_gosa_0109.csv')
df.to_csv('M:/UserDir/y_hcr_motohashi/Desktop/data_3/result/extratrees_gosa_0109.csv')


#カバー率(test)
a=rmse_test
b=(-1)*rmse_test
count_test=0
for i,g in enumerate(list_gosa):
    if g<a:
        if g>b:
            count_test=count_test+1

print('RMSE_test',100*count_test/len(list_gosa))

#カバー率(train)
a=rmse_train
b=(-1)*rmse_train
count_train=0
for i,g in enumerate(list_gosa):
    if g<a:
        if g>b:
            count_train=count_train+1

print('RMSE_train',100*count_train/len(list_gosa))


