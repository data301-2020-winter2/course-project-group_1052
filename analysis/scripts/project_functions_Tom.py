import pandas as pd
def load_and_process(path):
    df1 = pd.read_csv(path)
    
    df2 = (
        df1.drop(columns=['songName', 'ogLyric', 'kbLyric'])
            .rename(columns={'badword':'badWord'})
            .sort_values("ogArtist", ascending = True)
            .sort_values("year", ascending = True)
    )
    return df2

def badword_count(dataframe):
    df1 = (pd.DataFrame(dataframe['badWord']
                  .value_counts())
                  .reset_index()
                  .rename(columns={'index':'badWord','badWord':'frequency'})
                 )
    return df1

def unique_word_count(dataframe):
    df1 = (dataframe.groupby('ogArtist')['badWord']
             .nunique()
             .sort_values(ascending = False))
    
    return df1

def words_per_year(dataframe):
    
    df1 = dataframe.drop(columns = ['ogArtist', 'songName', 'category', 'ogLyric', 'kbLyric', 'count'])
    
    df2 = df1.loc[(df1['badWord'] == 'fuck') | (df1['badWord'] == 'shit') |(df1['badWord'] == 'damn') |(df1['badWord'] == 'man') |(df1['badWord'] == 'kiss')]
    
    df3 = df2.value_counts()
    
    df4 = df3.reset_index()
    
    df5 = df4.rename(columns={0:'count'})
    
    return df5