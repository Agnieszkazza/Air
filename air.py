import pandas as pd
data = pd.read_csv(r"C:\Users\zales\Documents\projekty\air\AirQuality.csv", sep=';')
df = pd.DataFrame(data)
print(df.columns)
df['Datetime'] = df['Date'] + ' ' + df['Time']
df['Datetime'] = pd.to_datetime(df['Datetime'], format='%d/%m/%Y %H.%M.%S')
print(df)
print(df[['Datetime']].head())                                  