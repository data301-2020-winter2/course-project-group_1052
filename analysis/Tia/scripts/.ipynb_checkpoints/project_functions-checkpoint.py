import panda as pd

def load_and_process(path):
    df1 = pd.read_csv(path)
    
    df2 = (df1.drop(columns='isPresent')
          .rename(columns={'badword':'badWord'})
          .sort_values(by='year',ascending = False)
          .loc[lambda x: x['year'] >= 2012]
          .reset_index(drop=True)
          .loc[:,'ogArtist':'year']
          )
    return df2