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