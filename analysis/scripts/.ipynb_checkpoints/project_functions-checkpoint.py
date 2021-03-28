import pandas as pd
import os 

def load_and_process(path, name):
    os.chdir('../../')
    df1 = pd.read_csv(path)
    
    df2 = (df1.drop(columns='isPresent')
          .rename(columns={'badword':'badWord'})
          .sort_values(by='year',ascending = False)
          .loc[lambda x: x['year'] >= 2012]
          .reset_index(drop=True)
          .loc[:,'ogArtist':'year']
          )
    os.chdir('analysis/' + name)
    return df2

def load_df(path):
    df1 = pd.read_csv(path)
    
    df2 = (df1.drop(columns=['isPresent','isCensored'])
           .rename(columns={'badword':'badWord'})
          )
    return df2

def badWorddf(df, column, word):
    df2 = df[df[column]==word]
    df2 = (pd.DataFrame(df2['year']
                      .value_counts())
          .reset_index()
          .rename(columns={'year':'value','index':'year'})
          .sort_values(by='year', ascending = False)
          .reset_index()
          .drop(columns='index')
         )
    return df2

def badWord_df(df,badWords):
    df2 = pd.DataFrame({'year':df['year'].unique().tolist()}).sort_values(by='year').reset_index(drop=True)
    for i in badWords:
        df3 = df[df['badWord']==i]['year'].value_counts()
        for j in range(2001,2020):
            if j not in df3.index:
                df3[j]=0
        df3 = df3.sort_index()
        df2[i]=df3.values
    return df2