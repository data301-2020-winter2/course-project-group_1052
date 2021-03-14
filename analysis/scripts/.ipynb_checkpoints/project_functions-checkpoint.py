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

def badWorddf(df, badWord):
    df2 = df[df['badWord']==badWord]
    df2 = (pd.DataFrame(df2['year']
                      .value_counts())
          .reset_index()
          .rename(columns={'year':'value','index':'year'})
          .sort_values(by='year', ascending = False)
          .reset_index()
          .drop(columns='index')
         )
    return df2