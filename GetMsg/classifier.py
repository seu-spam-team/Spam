#coding: utf-8
import re
import os
import time
import random
import jieba #处理中文，要加库
import nltk #处理英文
import sklearn #分类器用sklearn库
from sklearn.naive_bayes import MultinomialNB #多项式模式  可以换成伯努利之类的
import numpy as np
# pylab as pl
#import matplotlib.pyplot as plt #用于绘图的库
import pickle

#粗暴的词统计
def make_word_set(words_file):
    words_set = set() # set是一个集合，遍历所有训练集，找到有哪些词出现了
    with open(words_file,'rb') as fp:
        for line in fp.readlines():
            word = line.strip().decode("utf-8")
            if len(word)>0 and word not in words_set: #去重
                words_set.add(word)
    return words_set

# 文本处理，也就是样本生成过程
def text_processing(raw,flag='nltk'):
    test_data_list = []
    r='[’!"#$%&\'()*+,-./:;<=>?@[\\]^`{|}~]+'

    if flag == 'sklearn':
        word_cut = jieba.cut(raw, cut_all=False) # 精确模式，返回的结构是一个可迭代的genertor
        word_list = list(word_cut) # genertor转化为list，每个词unicode格式
        test_data_list.append(word_list) #训练集list [(词1，词2，词3)(词1，词2)]
    else:
        raw = re.sub(r,' ',raw)
        raw = raw.replace("\\r\\n"," ")
        raw = raw.replace("\\t"," ")
        raw = raw.replace("\\"," ")
        word_cut =  raw.split(' ')
        word_list = [tok.lower() for tok in word_cut if len(tok) > 2]
        test_data_list.append(word_list)
    

    return test_data_list

def words_dict(flag='nltk'):
    # 选取特征词
    rq = list()
    if flag == 'nltk':
        with open("2.pkl",'rb') as file:
            rq  = pickle.loads(file.read())
    else:
        with open("0.pkl",'rb') as file:
            rq  = pickle.loads(file.read())
    return rq


# 文本特征
def text_features(test_data_list, feature_words, flag='nltk'):
    def text_features(text, feature_words):
        text_words = set(text)
        ## -----------------------------------------------------------------------------------
        if flag == 'nltk':
            ## nltk特征 dict
            features = {word:1 if word in text_words else 0 for word in feature_words}
        elif flag == 'sklearn':
            ## sklearn特征 list
            features = [1 if word in text_words else 0 for word in feature_words]
        else:
            features = []
        ## -----------------------------------------------------------------------------------
        return features
    test_feature_list = [text_features(text, feature_words) for text in test_data_list]
    return test_feature_list

# 分类，同时输出准确率等
def text_classifier( test_feature_list, flag='nltk'):
    ## -----------------------------------------------------------------------------------
    if flag == 'nltk':
        with open("3.pkl",'rb') as file:
            rq  = pickle.loads(file.read())
        predict_result = rq.prob_classify(test_feature_list[0]).prob('c000008')
    elif flag == 'sklearn':
        ## sklearn分类器
        rq = MultinomialNB()
        with open("1.pkl",'rb') as file:
            rq  = pickle.loads(file.read())
        #test_accuracy =  rq.score(test_feature_list, ('c000008',))
        predict_result =  rq.predict_proba(test_feature_list)[0][0]
    else:
        predict_result = 0
    return predict_result

print ('开始')

## 文本预处理
folder_path = 'The hotels are the ones that rent out the tent. They are all lined up on the hotel grounds : )) So much for being one with nature, more like being one with a couple dozen tour groups and nature. I have about 100M of pictures from that trip. I can go through them and get you jpgs of my favorite scenic pictures.'
test_data_list = text_processing(folder_path)


## 文本特征提取和分类
# flag = 'nltk'
flag = 'nltk'

feature_words = words_dict(flag)
test_feature_list = text_features( test_data_list, feature_words, flag)
predict_result = text_classifier(test_feature_list, flag)

print(predict_result)
if predict_result > 0.5:
    print('垃圾邮件')
else:
    print('正常邮件')

