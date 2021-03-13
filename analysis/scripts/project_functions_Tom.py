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