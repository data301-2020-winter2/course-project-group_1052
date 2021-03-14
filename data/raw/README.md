# This directory will contain the raw dataset that we will be working with

Here you'll find the raw data files. There are currently 4 undedited data files:

* KB_censored-lyrics.csv

* KB_group-overview.csv

* KB_proportions.csv

* KB_word-overviews.csv

The dataframe we are using for this project is KB_censored-lyrics.csv

```python
    import pandas as pd
    df = pd.read_csv('data/raw/'KB_censored-lyrics.csv')
```

This code assumes that your current working directory is at course-project-group_1052
