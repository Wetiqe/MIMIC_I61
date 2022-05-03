# -*- coding: utf-8 -*-
"""
Created on Mon May  2 15:14:58 2022

@author: jja117
"""

# -*- coding: utf-8 -*-
import pickle
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import pandas as pd
import operator
import matplotlib.pyplot as plt

def My_knncomper_difftest(k_val):
    rightnumber = 0
    while True:
        try:
         if k_val == 1:
        
            k = int(input("Please input K value:\n"))
            predictlist =MYknn(X_test_std, X_train_std, Y_train, k)
            for m in range(len(X_test_std)):
                if predictlist[m] == Y_test[m]:
                    rightnumber = rightnumber + 1
            test_predict_score = (rightnumber / len(X_test_std))
            print("Test set prediction accuracy: \n",  test_predict_score * 100, "%")
            print("Error rate: \n", (1 -  test_predict_score) * 100, "%")
            print("Number of test set prediction errors: \n",(len(X_test_std)-rightnumber))
            rightnumber=0
            predictlist = MYknn(X_train_std, X_train_std, Y_train, k)
            for m in range(len(X_train_std)):
                if predictlist[m] == Y_train[m]:
                    rightnumber = rightnumber + 1
            Train_predict_score = (rightnumber / len(X_train_std))
            print("Train set prediction accuracy: \n", Train_predict_score * 100, "%")
            print("Error rate: \n", (1 - Train_predict_score) * 100, "%")
            print("Number of test set prediction errors: \n", (len(X_train_std) - rightnumber))
            break   
    
         elif k_val == 2:
             
            print('enter phase 2')
            Train_acc=[]
            Test_acc=[]
            acc=[]
            k = int(input("Please input maximum K value:\n"))
            for k in range(1,k):
                # print(k)
                test_predict_score=0
                rightnumber=0
                predictlist =MYknn(X_test_std, X_train_std, Y_train, k)
                for m in range(len(X_test_std)):
                    if predictlist[m] == Y_test[m]:
                        rightnumber = rightnumber + 1
                test_predict_score = (rightnumber / len(Y_test))
                print(test_predict_score*100)
                # print("Test set prediction accuracy: \n",  test_predict_score * 100, "%")
                Test_acc.append(  test_predict_score * 100)
                # print("Error rate: \n", (1 -  test_predict_score) * 100, "%")
                # print("Number of test set prediction errors: \n",(len(X_test_std)-rightnumber))
                rightnumber=0
                Train_predict_score=0
                predictlist = MYknn(X_train_std, X_train_std, Y_train, k)
                for m in range(len(X_train_std)):
                    if predictlist[m] == Y_train[m]:
                        rightnumber = rightnumber + 1
                Train_predict_score = (rightnumber / len(X_train_std))
                # print("Train set prediction accuracy: \n", Train_predict_score * 100, "%")
                Train_acc.append( Train_predict_score * 100)
                # print("Error rate: \n", (1 - Train_predict_score) * 100, "%")
                # print("Number of test set prediction errors: \n", (len(X_train_std) - rightnumber))       
             
            plt.plot(Test_acc)
            plt.title('Test_acc')
            plt.show()
            plt.plot(Train_acc)
            plt.title('Train_acc')
            plt.show()
            break
                
         else:
             break
            
        except:
            print("Error:Please input a number")S
            
            
            
            

        
def MYknn(test_object, training_object, training_object_target, K):
    predictlist = []
    for newpoint in test_object:
        dataSetSize = training_object.shape[0]
        diffMat= np.tile(newpoint, (dataSetSize, 1)) - training_object
        sqDistances = (diffMat**2).sum(axis=1)
        distances = sqDistances ** 0.5
        sortedDistIndicies = distances.argsort()
        classCount = {}
        for i in range(K):
            voteIlabel = training_object_target[sortedDistIndicies[i]]
            classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1  #Get the value of key from the map and return 0 without key
            sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
        predictlist.append(sortedClassCount[0][0])
    with open("MYKNN predict module", 'wb') as f:
        pickle.dump(MYknn, f)
    # print("Model saved successfully!\n")
    return predictlist





def training(case):
    while True:
         if case == 1:
             print('use knn')
             knn_comper_difftest()
             break
         elif case == 2:
             print('use my knn')
             k_val = int(input(           
                 'Please input: 1: input K . 2: k=[1:maximum]. : \n'))
             My_knncomper_difftest(k_val)
             break
         else:
             break

if __name__ == '__main__':
    MIMIC_Data=pd.read_csv('E:\\test2.csv') 
    MIMIC_Y = MIMIC_Data.pop('target').values
    MIMIC_X = MIMIC_Data.values
    X_train, X_test, Y_train, Y_test = train_test_split(MIMIC_X, MIMIC_Y, test_size=0.2,random_state=40)  # the value will sa
    
    std= StandardScaler()
    X_train_std=std.fit_transform(X_train)
    X_test_std=std.fit_transform(X_test)
    training(2)