import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer
from sklearn.decomposition import NMF
import pickle

ratings = pd.read_csv('ratings.csv')
movies=pd.read_csv('movies.csv')
df=pd.merge(ratings,movies,on='movieId')
df.drop(columns=["timestamp"],inplace=True)
df.set_index('userId')
df2=pd.pivot_table(df,index='userId',columns='title',values='rating')
imputer=KNNImputer(n_neighbors=2)
dfrecs=pd.DataFrame(imputer.fit_transform(df2), 
                       index = df2.index, 
                       columns = df2.columns)
#movie=pd.read_csv('Movie_recommender.csv')
model=NMF(n_components=20,init='random',random_state=42,max_iter=100)
model.fit(dfrecs)
Q=pd.DataFrame(model.components_,
              columns=dfrecs.columns,
              index=['feature1','feature2','feature3','feature4','feature5','feature6','feature7',
                     'feature8','feature9','feature10','feature11','feature12','feature13','feature14',
                     'feature15','feature16','feature17','feature18','feature19','feature20'])
P=pd.DataFrame(model.transform(dfrecs), 
                 columns=['feature1','feature2','feature3','feature4','feature5','feature6','feature7',
                     'feature8','feature9','feature10','feature11','feature12','feature13','feature14',
                     'feature15','feature16','feature17','feature18','feature19','feature20'],index=dfrecs.index)
recom_df=pd.DataFrame(np.dot(P,Q),index=dfrecs.index,columns=dfrecs.columns)
binary = pickle.dumps(model)
open('modelone.bin', 'wb').write(binary)
binary = open('modelone.bin','rb').read()
model_read = pickle.loads(binary)
#create new customer
BK = np.zeros(shape= (1,len(recom_df.columns))).tolist()[0]
BK_ratings = {'xXx (2002)': 4,'¡Three Amigos! (1986)':3}
for index,item in enumerate (dfrecs.columns):
    if item in BK_ratings.keys():
        print('Index of BK',index,item)
        BK[index]=BK_ratings[item]
BKdf=pd.DataFrame([BK],index = ['BK'],columns= dfrecs.columns)
dfrecsnew=pd.concat([dfrecs,BKdf])
print('df with BK ratings',dfrecsnew)
#run modell with BK in it
P_BK = model.transform(BKdf)
R_BK = np.dot(P_BK, Q)
RecomBK = pd.DataFrame(R_BK,index=['BK'],columns=dfrecs.columns)
recom_dfnew=pd.concat([recom_df,RecomBK])
print('This is ratings DF and BK ',recom_dfnew)

dfrecs.to_pickle("dfrecs.pkl")
recom_df.to_pickle("recom_df.pkl")
Q.to_pickle("Q.pkl")


#print('This is ratings DF ',ratings.head())
#print('This is movies DF ',movies.head())
#print('This is merged DF ',df.head())
#print('This is dfrecs DF ',dfrecs.head())
#print('This is Q ',Q.head())
#print('This is P ',P.head())
#print('This is recom_df ',recom_df.head())