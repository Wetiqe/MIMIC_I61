# -*- coding: utf-8 -*-
"""
Created on Mon May  2 15:14:58 2022

@author: jja117
"""

# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import operator
import matplotlib.pyplot as plt

def My_knncomper_difftest(k_max, X_train_std, X_test_std, Y_train, Y_test):
    Train_acc=[]; Test_acc=[]; acc=[]
    for k in range(1, k_max):
        test_predict_score=0
        rightnumber=0
        predictlist =MYknn(X_test_std, X_train_std, Y_train, k)
        for m in range(len(X_test_std)):
            if predictlist[m] == Y_test[m]:
                rightnumber = rightnumber + 1
        test_predict_score = (rightnumber / len(Y_test))
        print(k, "\t\t", test_predict_score*100)
        Test_acc.append(  test_predict_score * 100)

        rightnumber=0
        Train_predict_score=0
        predictlist = MYknn(X_train_std, X_train_std, Y_train, k)
        for m in range(len(X_train_std)):
            if predictlist[m] == Y_train[m]:
                rightnumber = rightnumber + 1
        Train_predict_score = (rightnumber / len(X_train_std))
        Train_acc.append( Train_predict_score * 100)
    plt.plot(Test_acc)
    plt.title('Test_acc')
    plt.show()
    plt.plot(Train_acc)
    plt.title('Train_acc')
    plt.show()
    

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
            print(sortedClassCount)
            print(type(sortedClassCount))
        predictlist.append(sortedClassCount[0][0])
        
        return predictlist
