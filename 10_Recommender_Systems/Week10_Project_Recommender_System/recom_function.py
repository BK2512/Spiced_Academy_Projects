import pickle
import numpy as np
import pandas as pd
import random

#nmf=pickle.load(open('modelone.bin','rb').read())

binary = open('modelone.bin','rb').read()
model_read = pickle.loads(binary)

dfrecs = pd.read_pickle("dfrecs.pkl")
recom_df = pd.read_pickle("recom_df.pkl")
Q = pd.read_pickle("Q.pkl")


#print(model_read.components_)

def nmf(query, k=10):
    new_user= np.zeros(shape= (1,len(recom_df.columns))).tolist()[0]
    new_user_ratings = query 
    for index,item in enumerate (dfrecs.columns):
        if item in new_user_ratings.keys():
            new_user [index]=new_user_ratings[item]
    newdf=pd.DataFrame([new_user],index = ['new_user'],columns= dfrecs.columns)
    #dfrecsnew=pd.concat([dfrecs,newdf])
    P_new = model_read.transform(newdf)
    R_new = np.dot(P_new, Q)
    Recomnew = pd.DataFrame(R_new,index=['new_user'],columns=dfrecs.columns)
    recom_dfnew=pd.concat([recom_df,Recomnew])
    
    top10=recom_dfnew.loc['new_user'].sort_values(ascending=False).head(10)
    top10=top10.index.to_list()
    return top10 

def Final(Top10,k=1):
    random.shuffle(Top10)
    Top1=Top10[:k]
    return Top1