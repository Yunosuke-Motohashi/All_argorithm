# All_argorithm

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import csv
from sklearn.utils.testing import all_estimators
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from statistics import mean, median,variance,stdev
import time
start = time.time()

# データの読み込み
dataset= pd.read_csv("C:/Users/yunom/Desktop/Output_python/Dataset_amedas.csv")
dataset = dataset.drop('Unnamed: 0', axis=1)

# データをラベルと入力データに分離する
target_col='MORE_AMP'
feature_col=dataset.columns[1:]
feature_col = np.array(feature_col)
y=np.array(dataset[target_col])
x=np.array(dataset[feature_col])

# classifierのすべてのアルゴリズムを取得する
allAlgorithms = all_estimators(type_filter = "regressor")

list_name=[]
for i in range(100):
    list_rmse_1=[]
    list_rmse_2=[]
    list_score_train=[]
    list_score_test=[]
    list_stdev=[]
# 学習用とテスト用に分離する
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=i)

    start = time.time()
    a=0
    for(name, algorithm) in allAlgorithms:
    # 各アルゴリズムのオブジェクトを生成
        clf = algorithm()
        a=a+1
        
    # 学習をして評価する
        if a<27:
            clf.fit(x_train, y_train)
            y_train_pred= clf.predict(x_train)
            y_test_pred = clf.predict(x_test)
            stdev_test= stdev(y_test)
            stdev_train= stdev(y_train)
            mse_train=mean_squared_error(y_train, y_train_pred)
            mse_test=mean_squared_error(y_test, y_test_pred)
            rmse_train= np.sqrt(mse_train)
            rmse_test= np.sqrt(mse_test)
            r_train=1-pow(rmse_train/stdev_train,2)
            r_test=1-pow(rmse_test/stdev_test,2)
            list_score_train.append(r_train)
            list_score_test.append(r_test)
            print(i,a,",")
            
            list_name.append(name)
            list_rmse_1.append(rmse_train)
            list_rmse_2.append(rmse_test)
            list_stdev.append(stdev_test)
    
            elapsed_time = time.time() - start
            print ("{0}".format(elapsed_time) + "[sec]")
    
        elif a>30 and a!=38:
            clf.fit(x_train, y_train)
            y_train_pred= clf.predict(x_train)
            y_test_pred = clf.predict(x_test)
            stdev_test= stdev(y_test)
            stdev_train= stdev(y_train)
            mse_train=mean_squared_error(y_train, y_train_pred)
            mse_test=mean_squared_error(y_test, y_test_pred)
            rmse_train= np.sqrt(mse_train)
            rmse_test= np.sqrt(mse_test)
            r_train=1-pow(rmse_train/stdev_train,2)
            r_test=1-pow(rmse_test/stdev_test,2)
            list_score_train.append(r_train)
            list_score_test.append(r_test)
            print(i,a,",")
            
            list_name.append(name)
            list_rmse_1.append(rmse_train)
            list_rmse_2.append(rmse_test)
            list_stdev.append(stdev_test)
    
            elapsed_time = time.time() - start
            print ("{0}".format(elapsed_time) + "[sec]")
    
    if i==0:
        rmse_1_l=pd.DataFrame({i+1:list_rmse_1})
        rmse_2_l=pd.DataFrame({i+1:list_rmse_2})
        r_train_l=pd.DataFrame({i+1:list_score_train})
        r_test_l=pd.DataFrame({i+1:list_score_test})
        name_l=pd.DataFrame({  'Name' : list_name})
        
        df_rmse_train=pd.concat([name_l,rmse_1_l],axis=1) 
        df_rmse_test=pd.concat([name_l,rmse_2_l],axis=1)
        df_r_train=pd.concat([name_l,r_train_l],axis=1)
        df_r_test=pd.concat([name_l,r_test_l],axis=1)
        
    else:
        rmse_1_l=pd.DataFrame({i+1:list_rmse_1})
        rmse_2_l=pd.DataFrame({i+1:list_rmse_2})
        r_train_l=pd.DataFrame({i+1:list_score_train})
        r_test_l=pd.DataFrame({i+1:list_score_test})
    
        df_rmse_train=pd.concat([df_rmse_train,rmse_1_l],axis=1) 
        df_rmse_test=pd.concat([df_rmse_test,rmse_2_l],axis=1)
        df_r_train=pd.concat([df_r_train,r_train_l],axis=1)
        df_r_test=pd.concat([df_r_test,r_test_l],axis=1)

list_name=[]
list_name=df_rmse_train["Name"]
rmse_train_avg=[]
rmse_test_avg=[]
r_train_avg=[]
r_test_avg=[]
rmse_train_avg=df_rmse_train.mean(axis='columns')
rmse_test_avg=df_rmse_test.mean(axis='columns')
r_train_avg=df_r_train.mean(axis='columns')
r_test_avg=df_r_test.mean(axis='columns')

rmse_train_max=df_rmse_train.max(axis=1)
rmse_train_min=df_rmse_train.min(axis=1)
rmse_train_max=pd.DataFrame({"Max":rmse_train_max})
rmse_train_min=pd.DataFrame({"Min":rmse_train_min})
df_rmse_train=pd.concat([df_rmse_train,rmse_train_max,rmse_train_min],axis=1)

rmse_test_max=df_rmse_test.max(axis=1)
rmse_test_min=df_rmse_test.min(axis=1)
rmse_test_max=pd.DataFrame({"Max":rmse_test_max})
rmse_test_min=pd.DataFrame({"Min":rmse_test_min})
df_rmse_test=pd.concat([df_rmse_test,rmse_test_max,rmse_test_min],axis=1)

r_train_max=df_r_train.max(axis=1)
r_train_min=df_r_train.min(axis=1)
r_train_max=pd.DataFrame({"Max":r_train_max})
r_train_min=pd.DataFrame({"Min":r_train_min})
df_r_train=pd.concat([df_r_train,r_train_max,r_train_min],axis=1)

r_test_max=df_r_test.max(axis=1)
r_test_min=df_r_test.min(axis=1)
r_test_max=pd.DataFrame({"Max":r_test_max})
r_test_min=pd.DataFrame({"Min":r_test_min})
df_r_test=pd.concat([df_r_test,r_test_max,r_test_min],axis=1)


rmse_train_max=df_rmse_train['Max'].values.tolist()
rmse_train_min=df_rmse_train['Min'].values.tolist()
rmse_test_max=df_rmse_test['Max'].values.tolist()
rmse_test_min=df_rmse_test['Min'].values.tolist()
r_train_max=df_r_train['Max'].values.tolist()
r_train_min=df_r_train['Min'].values.tolist()
r_test_max=df_r_test['Max'].values.tolist()
r_test_min= df_r_test['Min'].values.tolist()

df_allalgo=pd.DataFrame({  'Name' : list_name,
                         'RMSE_Train_Max' : rmse_train_max,'RMSE_Train_Min' : rmse_train_min,'RMSE_Train_Avg' : rmse_train_avg,
                         'RMSE_Test_Max' : rmse_test_max,'RMSE_Test_Min' : rmse_test_min,'RMSE_Test_Avg' : rmse_test_avg,
                         'R^2_Train_Max' : r_train_max,'R^2_Train_Min' : r_train_min,'R^2_Train_Avg' : r_train_avg,
                         'R^2_Test_Max' : r_test_max,'R^2_Test_Min' : r_test_min,'R^2_Test_Avg' : r_test_avg})

df_s = df_allalgo.sort_values('R^2_Test_Avg', ascending=False)
df_s =df_s.reset_index(drop=True)
df_s 

df_allalgo.to_csv('C:/Users/yunom/Desktop/Output_python/sklearn/all_algorithm.csv')
df_rmse_train.to_csv('C:/Users/yunom/Desktop/Output_python/sklearn/RMSE_Train.csv')
df_rmse_test.to_csv('C:/Users/yunom/Desktop/Output_python/sklearn/RMSE_Test.csv')
df_r_train.to_csv('C:/Users/yunom/Desktop/Output_python/sklearn/R^2_Train.csv')
df_r_test.to_csv('C:/Users/yunom/Desktop/Output_python/sklearn/R^2_Test.csv')
df_s.to_csv('C:/Users/yunom/Desktop/Output_python/sklearn/sort.csv')

