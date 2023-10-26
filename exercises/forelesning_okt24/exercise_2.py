#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sna


# %%
# Import file
df = pd.read_excel('DrillingData.xlsx')
# %%
# Get info about the data
# Vi ser at vi har int (vil ha floats) og objects 
df.info()                   
# %%
df.head(10)
df.tail(10)
# %%
# Får bare x2 nå, fordi den er den eneste som bare har numeric
df.describe()
# %%
# Object and int should be converted to float
df['x1'] = pd.to_numeric(df['x1'], errors='coerce') #coerce gjør at iinvalid entries blir NaN
df['x3'] = pd.to_numeric(df['x3'], errors='coerce') #coerce gjør at iinvalid entries blir NaN
df['x4'] = pd.to_numeric(df['x4'], errors='coerce') #coerce gjør at iinvalid entries blir NaN
df['y'] = pd.to_numeric(df['y'], errors='coerce') #coerce gjør at iinvalid entries blir NaN
df.head(10)
df.tail(10)
# df.describe() # alle kolonner vises nå, siden alle kolonner er Numeric
# %%
# To convert int to float
df['y'] = df['y'].astype(float)
df['x2'] = df['x2'].astype(float)

# Alternativt
# df['y'] = pd.to_numeric(df['y'], downcast='float')
# %%
# sjekker data på ny for å se etter nye feil
# ser non-null og int 64
df.info()
df.tail(40)
# %%
# Fjerner nå alle NaN
# ser først hvilke kolonner som har hvor mange blanks
missing_data = df.isnull().sum()
missing_data

df.dropna(inplace = True)
# %%
# Vi ser at vi har 21505 entries, og Non_Null kolonnen har bare 21505
df.info()
df.tail(10)
# %%
# Remove duplicated
dups = df.duplicated()
print(dups.any()) # Gir True, vi har altså duplicates i dataen vår
# %%
# Vi ser at vi har 5577 duplicates
print(df[dups])
# %%
# Remove duplicates
# Vi fjerner både NaN og duplicates og bør komme rundt 15000
df.drop_duplicates(inplace=True) #inplace overlagrer gjeldene fil

# %%
# Outlier removal (fortsetter neste time)
# %%
